# Proyecto Churn MLOps

- Author: Roberto Carlos Olguin Ledezma
- Enlace: https://github.com/sisroberto801/proyecto_churn_mlops.git

## 📋 Descripción del proyecto

Este proyecto implementa un sistema de predicción de churn (abandono de clientes) utilizando técnicas de Machine Learning.

El modelo analiza el comportamiento de los clientes para identificar patrones de riesgo de abandono, considerando factores demográficos y de uso como edad, antigüedad, saldo promedio, número de reclamos y frecuencia de uso de la aplicación móvil.

Este proyecto corresponde a una práctica inicial del módulo de MLOps con el objetivo de construir una estructura básica de trabajo para un proyecto de Machine Learning que permita:

- Preparar datos
- Entrenar un modelo
- Evaluar métricas
- Guardar el modelo entrenado
- Exponer el modelo mediante una API
- Ejecutar pruebas básicas

## 🏗️ Estructura del proyecto

```text
proyecto_churn_mlops
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── RESUMEN_EXPERIMENTO.md
├── requirements.txt
├── api/
│   ├── __init__.py
│   └── main.py
├── data/
│   └── descripcion_dataset.md
├── docs/
│   └── metricas_modelo.md
├── models/
│   └── .gitkeep
├── notebooks/
│   └── .gitkeep
├── src/
│   ├── entrenar_modelo.py
│   ├── evaluar_modelo.py
│   └── preparar_datos.py
└── tests/
    ├── __init__.py
    ├── test_api.py
    └── test_api_nueva.py
```

### Carpetas principales

- `api/`: contiene la API FastAPI (`main.py`) para exponer el modelo
- `data/`: contiene los datos del proyecto y descripción del dataset
- `docs/`: contiene documentación y métricas de evaluación
- `models/`: contiene el modelo entrenado (se genera al ejecutar)
- `notebooks/`: contiene análisis exploratorios (actualmente vacía)
- `src/`: contiene los scripts principales del modelo (preparar, entrenar, evaluar)
- `tests/`: contiene pruebas automáticas de la API

### Archivos de configuración

- `requirements.txt`: dependencias Python del proyecto
- `Dockerfile`: configuración para construir la imagen Docker
- `.dockerignore`: archivos a ignorar en la construcción Docker
- `.gitignore`: archivos a ignorar en el control de versiones
- `README.md`: documentación principal del proyecto
- `RESUMEN_EXPERIMENTO.md`: detalles completos del experimento ML

## 🚀 Instalación y Ejecución

### 📋 Requisitos Previos
- Python 3.8+
- pip
- Git
- Docker (opcional, para ejecución con contenedores)

### 🔧 Instalación
```bash
# Clonar repositorio
git clone https://github.com/sisroberto801/proyecto_churn_mlops.git
cd proyecto_churn_mlops

# Instalar dependencias
pip install -r requirements.txt
```

## 🏃‍♂️ Flujo Completo de Ejecución

### Paso 1: Preparar Datos
```bash
python src/preparar_datos.py
```
✅ **Resultado esperado:**
- Genera `data/train.csv` y `data/test.csv`
- Crea 16 registros de ejemplo
- Divide datos 75% entrenamiento, 25% prueba

### Paso 2: Entrenar Modelo
```bash
python src/entrenar_modelo.py
```
✅ **Resultado esperado:**
```
Modelo entrenado correctamente.
Modelo guardado en: /path/to/models/modelo_churn_v1.joblib
Metadatos guardados en: /path/to/models/modelo_churn_v1_metadata.json
✅ Random Forest entrenado
🎉 Ambos modelos entrenados
```
📁 **Archivos generados:**
- `models/modelo_churn_v1.joblib` - Modelo principal
- `models/modelo_churn_v1_metadata.json` - Metadatos completos
- `models/modelo_rf.pkl` - Modelo Random Forest alternativo

### Paso 3: Evaluar Modelo
```bash
python src/evaluar_modelo.py
```
✅ **Resultado esperado:**
- Actualiza `docs/metricas_modelo.md` con métricas
- Calcula: Accuracy, Precision, Recall, F1-score, ROC-AUC
- Genera reporte de rendimiento

### Paso 4: Iniciar API
```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```
✅ **Resultado esperado:**
```
INFO:     Will watch for changes in these directories: ['/path/to/proyecto_churn_mlops']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [XXXX]
INFO:     Started server process [XXXX]
INFO:     Application startup complete.
```
🌐 **Endpoints disponibles:**
- `GET /` - Mensaje de bienvenida
- `GET /health` - Estado del servicio
- `GET /info` - **MEJORA TÉCNICA**: Metadatos del modelo
- `POST /predict` - Predicción con validaciones mejoradas

## 🧪 Pruebas de la API

### Opción A: Pruebas Básicas (Terminal 2)
```bash
# En una nueva terminal - PREVIAMENTE DEBERÁ ESTAR CORRIENDO LA API
python tests/test_api_nueva.py
```

### Opción B: Pruebas Completas (Terminal 2) - **RECOMENDADO**
```bash
# En una nueva terminal - PREVIAMENTE DEBERÁ ESTAR CORRIENDO LA API
python tests/test_api_completa.py
```
✅ **Incluye:**
- ✅ Pruebas de todos los endpoints
- ✅ Casos válidos (4 escenarios diferentes)
- ✅ Casos inválidos (campo faltante, tipo incorrecto, fuera de rango, valores negativos)
- ✅ Validación de mejoras técnicas

### Opción C: Pruebas Manuales (Terminal 2)
**PREVIAMENTE DEBERÁ ESTAR CORRIENDO LA API**

#### 1. Verificar Salud del Servicio
```bash
curl http://localhost:8000/health
```
✅ **Esperado:** `{"estado":"ok","modelo_disponible":true,"metadatos_disponibles":true}`

#### 2. Obtener Información del Modelo (**MEJORA TÉCNICA**)
```bash
curl http://localhost:8000/info
```
✅ **Esperado:** Metadatos completos con versión, autor, fecha, variables

#### 3. Realizar Predicción Válida
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "edad": 35,
    "antiguedad_meses": 24,
    "saldo_promedio": 50000,
    "reclamos": 1,
    "usa_app": 1
  }'
```
✅ **Esperado:** Respuesta enriquecida con nivel de riesgo, descripción, recomendación

#### 4. Probar Validación (Campo Faltante)
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "edad": 35,
    "antiguedad_meses": 24,
    "saldo_promedio": 50000
  }'
```
✅ **Esperado:** Error 422 con "Field required"

#### 5. Probar Validación (Tipo Incorrecto)
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "edad": "treinta",
    "antiguedad_meses": 24,
    "saldo_promedio": 50000,
    "reclamos": 1,
    "usa_app": 1
  }'
```
✅ **Esperado:** Error 422 con "Input should be a valid integer"

#### 6. Probar Validación (Valor Fuera de Rango)
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "edad": 150,
    "antiguedad_meses": 24,
    "saldo_promedio": 50000,
    "reclamos": 1,
    "usa_app": 1
  }'
```
✅ **Esperado:** Error 422 con "Input should be less than or equal to 100"

#### 7. Probar Validación (Saldo Excesivo)
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "edad": 35,
    "antiguedad_meses": 24,
    "saldo_promedio": 2000000,
    "reclamos": 1,
    "usa_app": 1
  }'
```
✅ **Esperado:** Error 422 con "El saldo promedio no puede superar $1,000,000"

## 🌐 Acceso a Documentación

### Swagger UI (Navegador)
```
http://localhost:8000/docs
```

### ReDoc (Navegador)
```
http://localhost:8000/redoc
```

## 📁 Verificación de Archivos Generados

### Verificar Modelo y Metadatos
```bash
ls -la models/
```
✅ **Debería mostrar:**
- `modelo_churn_v1.joblib` - Modelo principal (v1)
- `modelo_churn_v1_metadata.json` - Metadatos completos
- `modelo_rf.pkl` - Modelo Random Forest alternativo

### Verificar Contenido de Metadatos
```bash
cat models/modelo_churn_v1_metadata.json
```
✅ **Debería mostrar:**
```json
{
  "nombre_modelo": "modelo_churn_v1",
  "version": "1.0",
  "autor": "Roberto Carlos Olguin Ledezma",
  "fecha_entrenamiento": "2026-06-13T15:48:53.667434",
  "algoritmo": "Regresión Logística con StandardScaler",
  "variables_entrada": ["edad", "antiguedad_meses", "saldo_promedio", "reclamos", "usa_app"],
  "variable_objetivo": "churn",
  "metricas": {"accuracy": 1.0, "precision": 1.0, "recall": 1.0, "f1_score": 1.0}
}
```

### Verificar Métricas
```bash
cat docs/metricas_modelo.md
```
✅ **Debería mostrar tabla con:**
- Accuracy: 1.0000
- Precision: 1.0000
- Recall: 1.0000
- F1-score: 1.0000
- AUC: 1.0000

## 🐳 Opción Docker (Alternativa)

### Construir Imagen
```bash
docker build -t churn-api-olguin .
```

### Ejecutar Contenedor
```bash
docker run -d -p 8000:8000 --name churn-api-container churn-api-olguin
```

### Verificar Contenedor
```bash
docker ps
docker logs churn-api-container
```

## 🛑 Detener Servicios

### Detener API Local
```bash
# En la terminal donde corre uvicorn
Ctrl + C
```

### Detener Contenedor Docker
```bash
docker stop churn-api-container
docker rm churn-api-container
```

## ✅ Checklist de Verificación - **Actividad API Predictiva**

### 📋 Archivos Generados
- [ ] `modelo_churn_v1.joblib` - Modelo serializado ✅
- [ ] `modelo_churn_v1_metadata.json` - Metadatos completos ✅
- [ ] `docs/metricas_modelo.md` - Métricas de evaluación ✅
- [ ] `data/train.csv` y `data/test.csv` - Datos preparados ✅

### 🌐 Endpoints API
- [ ] `GET /` - Mensaje de bienvenida con autor ✅
- [ ] `GET /health` - Estado del servicio y modelo ✅
- [ ] `GET /info` - **MEJORA TÉCNICA**: Metadatos del modelo ✅
- [ ] `POST /predict` - Predicción con validaciones mejoradas ✅

### 🧪 Pruebas de Validación
- [ ] **Caso válido**: Predicción exitosa con respuesta enriquecida ✅
- [ ] **Campo faltante**: Error 422 "Field required" ✅
- [ ] **Tipo incorrecto**: Error 422 "Input should be a valid integer" ✅
- [ ] **Valor fuera de rango**: Error 422 "Input should be less than or equal to 100" ✅
- [ ] **Saldo excesivo**: Error 422 "El saldo promedio no puede superar $1,000,000" ✅

### 🚀 Mejoras Técnicas Implementadas
- [ ] **Endpoint `/info`** con metadatos del modelo ✅
- [ ] **Validaciones robustas** (edad 18-100, saldo máximo $1M) ✅
- [ ] **Respuesta enriquecida** (nivel de riesgo, descripción, recomendación) ✅
- [ ] **Autor identificado** en todas las respuestas ✅
- [ ] **Metadatos automáticos** con fecha de entrenamiento ✅

### 📊 Ejecución Completa
- [ ] Dependencias instaladas (`pip install -r requirements.txt`) ✅
- [ ] Script de entrenamiento ejecutado correctamente ✅
- [ ] API iniciada y funcionando en `http://localhost:8000` ✅
- [ ] Pruebas automatizadas pasando exitosamente ✅
- [ ] Documentación accesible (Swagger/ReDoc) ✅

### 🎯 Cumplimiento Actividad
- [ ] **8/8 puntos** - Todos los requisitos cumplidos ✅
- [ ] **Evidencias listas** para PDF y entrega ✅
- [ ] **Reflexión final** preparada ✅

## 🚨 Troubleshooting

### Error: "ModuleNotFoundError"
```bash
# Asegúrate de estar en el directorio correcto
cd proyecto_churn_mlops
pip install -r requirements.txt
```

### Error: "Modelo no disponible"
```bash
# Asegúrate de haber entrenado el modelo primero
python src/entrenar_modelo.py
```

### Error: Puerto 8000 en uso
```bash
# Usar otro puerto
uvicorn api.main:app --reload --port 8001
```

## 📞 Soporte

Para cualquier problema, verifica:
1. Python versión 3.8+
2. Todas las dependencias instaladas
3. Ejecución en orden correcto
4. Archivos generados existen

## 📄 Documentación adicional

- [CUMPLIMIENTO_ACTIVIDAD.md](CUMPLIMIENTO_ACTIVIDAD.md) - Checklist de requisitos
- [RESUMEN_EXPERIMENTO.md](RESUMEN_EXPERIMENTO.md) - Detalles del experimento ML

## 🔧 Detalles técnicos

### Algoritmos implementados
1. **Regresión Logística**: Modelo base con regularización L2
   - Hiperparámetro C: 1.0 (modificado de 0.1)
   - Max iteraciones: 1000
   - Escalado: StandardScaler

2. **Random Forest**: Ensemble de árboles de decisión
   - N estimators: 300 (modificado de 200)
   - Max depth: 20 (modificado de 15)
   - Random state: 42

### Métricas evaluadas
- Accuracy: Precisión general del modelo
- Precision: Confianza en predicciones positivas
- Recall: Capacidad de detectar clientes con churn
- F1-score: Balance entre precision y recall
- **ROC-AUC**: Capacidad de discriminación del modelo (nueva)

### Arquitectura del proyecto
- **Datos**: CSV con 16 registros de ejemplo
- **Preprocesamiento**: Limpieza de duplicados y nulos
- **División**: 75% entrenamiento, 25% prueba (stratified)
- **API**: FastAPI con endpoints `/`, `/health`, `/info`, `/predict`
- **Evaluación**: Métricas guardadas en docs/metricas_modelo.md

## 🚀 MEJORAS TÉCNICAS IMPLEMENTADAS

### 1. Endpoint `/info` (Informativo)
- Muestra metadatos completos del modelo
- Incluye versión, autor, fecha de entrenamiento
- Lista variables utilizadas y métricas

### 2. Validaciones mejoradas en `/predict`
- **Rangos de edad**: 18-100 años
- **Validación de saldo**: Máximo $1,000,000
- **Tipos de datos**: Verificación estricta
- **Valores negativos**: Rechazo automático

### 3. Respuesta enriquecida de `/predict`
- **Nivel de riesgo**: bajo/medio/alto según probabilidad
- **Descripción**: Interpretación del resultado
- **Recomendación**: Acción sugerida según perfil
- **Autor**: Identificación del desarrollador

### 4. Metadatos del modelo
- Archivo JSON con información completa
- Fecha y hora de entrenamiento
- Hiperparámetros configurados
- Métricas de rendimiento

### 5. Pruebas exhaustivas
- Casos válidos e inválidos
- Validación de tipos y rangos
- Pruebas de integración completas

## 📚 Control de versiones

Este proyecto utiliza Git para registrar cambios y GitHub para respaldar el repositorio en la nube.

El uso de commits permite mantener trazabilidad sobre los cambios realizados en el código, la documentación y la estructura del proyecto.