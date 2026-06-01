# Proyecto Churn MLOps

- Author: Roberto Carlos Olguin Ledezma
- Enlace: https://github.com/sisroberto801/proyecto_churn_mlops.git

Este proyecto corresponde a una práctica inicial del módulo de MLOps.

## 🚀 Instrucciones de instalación

```bash
# Clonar repositorio
git clone https://github.com/sisroberto801/proyecto_churn_mlops.git
cd proyecto_churn_mlops

# Instalar dependencias
pip install -r requirements.txt
```

## 🏃‍♂️ Pasos de ejecución

### Paso 1: Preparar datos
```bash
python src/preparar_datos.py
```
- Genera datos de ejemplo
- Divide en conjuntos de entrenamiento y prueba
- Crea archivos `data/train.csv` y `data/test.csv`

### Paso 2: Entrenar modelos
```bash
python src/entrenar_modelo.py
```
- Entrena **Regresión Logística** (modelo base)
- Entrena **Random Forest** (nuevo modelo)
- Guarda modelos en `models/modelo_churn.pkl` y `models/modelo_rf.pkl`

### Paso 3: Evaluar modelos
```bash
python src/evaluar_modelo.py
```
- Calcula métricas (Accuracy, Precision, Recall, F1-score, ROC-AUC)
- Guarda resultados en `docs/metricas_modelo.md`

### Paso 4: Iniciar API
```bash
uvicorn api.main:app --reload
```
- Inicia servidor FastAPI en `http://localhost:8000`
- Endpoint disponible: `/predict`

### Paso 5: Probar API (opcional)
```bash
python tests/test_api_nueva.py
```
- Ejecuta prueba automatizada de la API

### Verificación rápida
```bash
curl http://localhost:8000/health
```

### Estructura generada
- `data/`: archivos CSV de datos
- `models/`: modelos entrenados (.pkl)
- `docs/`: métricas de evaluación

## 📄 Documentación del experimento
Para detalles completos del experimento realizado, consulta el [RESUMEN_EXPERIMENTO.md](RESUMEN_EXPERIMENTO.md).

El objetivo es construir una estructura básica de trabajo para un proyecto de Machine Learning que permita:

- Preparar datos.
- Entrenar un modelo.
- Evaluar métricas.
- Guardar el modelo entrenado.
- Exponer el modelo mediante una API.
- Ejecutar pruebas básicas.

## Problema del proyecto

Este proyecto implementa un sistema de predicción de churn (abandono de clientes) utilizando técnicas de Machine Learning.

El modelo analiza el comportamiento de los clientes para identificar patrones de riesgo de abandono, considerando factores demográficos y de uso como edad, antigüedad, saldo promedio, número de reclamos y frecuencia de uso de la aplicación móvil.

## Estructura del proyecto

```text
proyecto_churn_mlops
├── data
├── notebooks
├── src
├── models
├── api
├── tests
├── docs
├── README.md
└── requirements.txt
```

## Carpetas principales

- `data`: contiene los datos del proyecto.
- `notebooks`: contiene análisis exploratorios (actualmente vacía).
- `src`: contiene los scripts principales del modelo.
- `models`: contiene el modelo entrenado (se genera al ejecutar).
- `api`: contiene la API del modelo.
- `tests`: contiene pruebas automáticas.
- `docs`: contiene documentación y métricas.

## Flujo inicial del proyecto

El flujo básico será:

1. Preparar los datos.
2. Entrenar el modelo.
3. Evaluar el modelo.
4. Guardar las métricas.
5. Crear una API básica.
6. Probar el funcionamiento inicial.
## Control de versiones
Este proyecto utiliza Git para registrar cambios y GitHub para respaldar el repositorio en la nube.

El uso de commits permite mantener trazabilidad sobre los cambios realizados en el código, la documentación y la estructura del proyecto.

### Algoritmos
- Regresión Logística (base)
- Random Forest (nuevo)

### Hiperparámetros modificados
- Random Forest: n_estimators=300, max_depth=20

### Métricas
- Accuracy, Precision, Recall, F1-score, **ROC-AUC (nueva)**

### Nueva prueba de API
- Archivo: `tests/test_api_nueva.py`
- Ejecutar con: `python tests/test_api_nueva.py`

## 📋 Detalles técnicos del experimento

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
- **API**: FastAPI con endpoint /predict
- **Evaluación**: Métricas guardadas en docs/metricas_modelo.md

### Flujo de ejecución
1. `python src/preparar_datos.py` - Genera datos y divide train/test
2. `python src/entrenar_modelo.py` - Entrena ambos algoritmos
3. `python src/evaluar_modelo.py` - Calcula métricas y guarda resultados
4. `uvicorn api.main:app --reload` - Inicia API
5. `python tests/test_api_nueva.py` - Prueba automática de API