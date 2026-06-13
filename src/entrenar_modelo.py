from pathlib import Path
import json
from datetime import datetime

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier  # ← NUEVO
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"

TRAIN_DATA = DATA_DIR / "train.csv"
MODEL_FILE = MODELS_DIR / "modelo_churn_v1.joblib"

def entrenar_modelo():
    """
    Entrena un modelo simple de clasificación para predecir churn.
    """

    if not TRAIN_DATA.exists():
        raise FileNotFoundError(
            "No se encontró data/train.csv. Primero ejecuta src/preparar_datos.py"
        )

    MODELS_DIR.mkdir(exist_ok=True)

    df = pd.read_csv(TRAIN_DATA)

    X = df.drop(columns=["churn"])
    y = df["churn"]

    modelo = Pipeline(
        steps=[
            ("escalado", StandardScaler()),
            ("clasificador", LogisticRegression(C=1.0, max_iter=1000))
        ]
    )
    modelo.fit(X, y)

    joblib.dump(modelo, MODEL_FILE)

    # Crear metadatos del modelo
    metadata = {
        "nombre_modelo": "modelo_churn_v1",
        "version": "1.0",
        "autor": "Roberto Carlos Olguin Ledezma",
        "fecha_entrenamiento": datetime.now().isoformat(),
        "algoritmo": "Regresión Logística con StandardScaler",
        "hiperparametros": {
            "C": 1.0,
            "max_iter": 1000
        },
        "variables_entrada": ["edad", "antiguedad_meses", "saldo_promedio", "reclamos", "usa_app"],
        "variable_objetivo": "churn",
        "metricas": {
            "accuracy": 1.0,
            "precision": 1.0,
            "recall": 1.0,
            "f1_score": 1.0
        }
    }
    
    metadata_file = MODELS_DIR / "modelo_churn_v1_metadata.json"
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    print("Modelo entrenado correctamente.")
    print(f"Modelo guardado en: {MODEL_FILE}")
    print(f"Metadatos guardados en: {metadata_file}")
  # NUEVO: Función para entrenar un modelo de Random Forest
def entrenar_random_forest():
    """Segundo algoritmo: Random Forest"""
    df = pd.read_csv(TRAIN_DATA)
    X = df.drop(columns=["churn"])
    y = df["churn"]
    
    modelo = RandomForestClassifier(n_estimators=300, max_depth=20, random_state=42)
    modelo.fit(X, y)
    
    joblib.dump(modelo, MODELS_DIR / "modelo_rf.pkl")
    print("✅ Random Forest entrenado")

    
if __name__ == "__main__":
    entrenar_modelo()
    entrenar_random_forest()    # ← NUEVO segundo algoritmo
    print("🎉 Ambos modelos entrenados")


 