from pathlib import Path
import json

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator

BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_FILE = BASE_DIR / "models" / "modelo_churn_v1.joblib"
METADATA_FILE = BASE_DIR / "models" / "modelo_churn_v1_metadata.json"

app = FastAPI(
    title="API de Predicción de Churn",
    version="0.1.0",
    description="API básica para consumir un modelo de Machine Learning."
)

class Cliente(BaseModel):
    edad: int = Field(..., ge=18, le=100, description="Edad del cliente (18-100 años)")
    antiguedad_meses: int = Field(..., ge=0, description="Antigüedad en meses")
    saldo_promedio: float = Field(..., ge=0, description="Saldo promedio mensual")
    reclamos: int = Field(..., ge=0, description="Número de reclamos")
    usa_app: int = Field(..., ge=0, le=1, description="Usa aplicación móvil (0=No, 1=Sí)")

    @validator('saldo_promedio')
    def validar_saldo(cls, v):
        if v > 1000000:
            raise ValueError('El saldo promedio no puede superar $1,000,000')
        return v

def cargar_modelo():
    """
    Carga el modelo entrenado si existe.
    """
    if not MODEL_FILE.exists():
      return None

    return joblib.load(MODEL_FILE)

def cargar_metadatos():
    """
    Carga los metadatos del modelo si existen.
    """
    if not METADATA_FILE.exists():
        return None
    
    with open(METADATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def determinar_nivel_riesgo(probabilidad):
    """
    Determina el nivel de riesgo basado en la probabilidad.
    """
    if probabilidad is None:
        return "desconocido"
    elif probabilidad < 0.3:
        return "bajo"
    elif probabilidad < 0.7:
        return "medio"
    else:
        return "alto"

@app.get("/")
def inicio():
    return {
        "mensaje": "Servicio ML-Ops activo",
        "estado": "ok",
        "autor": "Roberto Carlos Olguin Ledezma"
    }

@app.get("/health")
def health():
    return {
        "estado": "ok",
        "modelo_disponible": MODEL_FILE.exists(),
        "metadatos_disponibles": METADATA_FILE.exists()
    }

@app.get("/info")
def info():
    """
    Endpoint informativo con detalles del modelo.
    MEJORA TÉCNICA PERSONAL
    """
    metadatos = cargar_metadatos()
    
    if metadatos is None:
        return {
            "mensaje": "Metadatos no disponibles",
            "modelo_disponible": MODEL_FILE.exists()
        }
    
    return {
        "nombre_modelo": metadatos.get("nombre_modelo"),
        "version": metadatos.get("version"),
        "autor": metadatos.get("autor"),
        "fecha_entrenamiento": metadatos.get("fecha_entrenamiento"),
        "algoritmo": metadatos.get("algoritmo"),
        "variables_entrada": metadatos.get("variables_entrada"),
        "variable_objetivo": metadatos.get("variable_objetivo"),
        "metricas": metadatos.get("metricas")
    }

@app.post("/predict")
def predict(cliente: Cliente):
    modelo = cargar_modelo()

    if modelo is None:
        raise HTTPException(
            status_code=503,
            detail="El modelo aún no está disponible. Primero se debe entrenar el modelo."
        )

    datos = pd.DataFrame([cliente.model_dump()])

    prediccion = int(modelo.predict(datos)[0])

    probabilidad = None
    if hasattr(modelo, "predict_proba"):
        probabilidad = float(modelo.predict_proba(datos)[0][1])

    # MEJORA TÉCNICA: Nivel de riesgo y recomendaciones
    nivel_riesgo = determinar_nivel_riesgo(probabilidad)
    
    # Generar descripción y recomendación
    if prediccion == 1:
        descripcion = "El cliente presenta alta probabilidad de abandono"
        if nivel_riesgo == "alto":
            recomendacion = "Contactar inmediatamente con ofertas especiales y atención prioritaria"
        elif nivel_riesgo == "medio":
            recomendacion = "Programar llamada de retención dentro de 48 horas"
        else:
            recomendacion = "Enviar campaña de fidelización personalizada"
    else:
        descripcion = "El cliente tiene baja probabilidad de abandono"
        recomendacion = "Mantener servicio regular y programa de lealtad"

    return {
        "churn_predicho": prediccion,
        "probabilidad_churn": probabilidad,
        "nivel_riesgo": nivel_riesgo,
        "descripcion": descripcion,
        "recomendacion": recomendacion,
        "autor": "Roberto Carlos Olguin Ledezma"
    }
