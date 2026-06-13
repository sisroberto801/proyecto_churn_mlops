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

## 🚀 Instrucciones de instalación

### Requisitos previos
- Python 3.8+
- pip
- Docker (opcional, para ejecución con contenedores)

### Instalación
```bash
# Clonar repositorio
git clone https://github.com/sisroberto801/proyecto_churn_mlops.git
cd proyecto_churn_mlops

# Instalar dependencias
pip install -r requirements.txt
```

## 🏃‍♂️ Flujo de ejecución

El flujo básico del proyecto es:

1. **Preparar los datos** - Generar datos de ejemplo y dividir en train/test
2. **Entrenar el modelo** - Entrenar algoritmos de ML
3. **Evaluar el modelo** - Calcular métricas de rendimiento
4. **Iniciar la API** - Exponer el modelo mediante servicio web
5. **Probar el funcionamiento** - Verificar que todo funciona correctamente

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

#### Opción A: Ejecución local
```bash
uvicorn api.main:app --reload
```
- Inicia servidor FastAPI en `http://localhost:8000`
- Endpoint disponible: `/predict`

#### Opción B: Ejecución con Docker
```bash
# Construir imagen Docker
docker build -t churn-api-olguin .

# Ejecutar contenedor
docker run -d -p 8000:8000 --name churn-api-container churn-api-olguin
```
- Construye y ejecuta la API en un contenedor Docker
- La API estará disponible en `http://localhost:8000`
- Para verificar el estado: `docker ps`

### Paso 5: Probar API
```bash
python tests/test_api_nueva.py
```
- Ejecuta prueba automatizada de la API

### Verificación rápida
```bash
curl http://localhost:8000/health
```

## 🐳 Administración de contenedores Docker

```bash
# Ver contenedores en ejecución
docker ps

# Ver logs del contenedor
docker logs churn-api-container

# Detener contenedor
docker stop churn-api-container

# Eliminar contenedor
docker rm churn-api-container

# Eliminar imagen
docker rmi churn-api-olguin
```

## 📊 Estructura generada

Después de ejecutar el flujo completo, se generarán los siguientes archivos:

- `data/`: archivos CSV de datos
- `models/`: modelos entrenados (.pkl)
- `docs/`: métricas de evaluación

## 📄 Documentación del experimento

Para detalles completos del experimento realizado, consulta el [RESUMEN_EXPERIMENTO.md](RESUMEN_EXPERIMENTO.md).

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
- **API**: FastAPI con endpoint /predict
- **Evaluación**: Métricas guardadas en docs/metricas_modelo.md

## 📚 Control de versiones

Este proyecto utiliza Git para registrar cambios y GitHub para respaldar el repositorio en la nube.

El uso de commits permite mantener trazabilidad sobre los cambios realizados en el código, la documentación y la estructura del proyecto.