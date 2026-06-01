# Resumen del Experimento de Modelo Mejorado

## Parte A. Evidencia Base

### Estructura del proyecto
```
proyecto_churn_mlops/
├── data/
│   ├── churn_clientes.csv
│   ├── train.csv
│   └── test.csv
├── src/
│   ├── preparar_datos.py
│   ├── entrenar_modelo.py
│   └── evaluar_modelo.py
├── api/
│   ├── __init__.py
│   └── main.py
├── models/
│   ├── modelo_churn.pkl
│   └── modelo_rf.pkl
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_api_nueva.py
├── docs/
│   └── metricas_modelo.md
├── requirements.txt
├── .gitignore
└── README.md
```

### requirements.txt
```
pandas
scikit-learn
joblib
fastapi
uvicorn
pytest
httpx
```

## Parte B. Mini Experimento del Modelo

### Rama creada
- **Nombre**: `experimento_modelo_mejorado`

### Modificaciones realizadas

#### 1. Segundo algoritmo implementado ✅
- **Random Forest**: Añadido al archivo `src/entrenar_modelo.py`
- **Archivo**: `src/entrenar_modelo.py`

#### 2. Hiperparámetros modificados ✅
- **Regresión Logística**: C cambiado de 0.1 a 1.0
- **Random Forest**: 
  - n_estimators: 200 → 300
  - max_depth: 15 → 20

#### 3. Métrica adicional agregada ✅
- **ROC-AUC**: Añadida en `src/evaluar_modelo.py`
- **Archivo**: `src/evaluar_modelo.py`

#### 4. Nueva prueba de API ✅
- **Archivo**: `tests/test_api_nueva.py`
- **Ejecución**: `python tests/test_api_nueva.py`

#### 5. Documentación técnica mejorada ✅
- **Archivo**: `README.md`
- **Secciones agregadas**: Detalles técnicos, arquitectura, flujo de ejecución

## Parte C. Evidencia del Experimento

### Resultados obtenidos

#### Métricas del modelo
| Métrica | Valor |
|---|---:|
| Accuracy | 1.0000 |
| Precision | 1.0000 |
| Recall | 1.0000 |
| F1-score | 1.0000 |
| **ROC-AUC** | **1.0000** |

#### Captura de ejecución
```
Datos preparados correctamente.
Archivo de entrenamiento: /Users/rolguin/Documents/ugrm/modulo16/proyecto_churn_mlops/data/train.csv
Archivo de prueba: /Users/rolguin/Documents/ugrm/modulo16/proyecto_churn_mlops/data/test.csv

Modelo entrenado correctamente.
Modelo guardado en: /Users/rolguin/Documents/ugrm/modulo16/proyecto_churn_mlops/models/modelo_churn.pkl
✅ Random Forest entrenado
🎉 Ambos modelos entrenados

Modelo evaluado correctamente.
Métricas guardadas en: /Users/rolguin/Documents/ugrm/modulo16/proyecto_churn_mlops/docs/metricas_modelo.md
ROC-AUC: 1.0000
```

### Interpretación de resultados

#### ¿Qué cambió?
1. **Hiperparámetros**: Se ajustó la regularización en Regresión Logística (C: 0.1→1.0) y se aumentó la complejidad del Random Forest (n_estimators: 200→300, max_depth: 15→20)
2. **Métricas**: Se agregó ROC-AUC como métrica de evaluación adicional
3. **Algoritmos**: Se implementó Random Forest como segundo modelo
4. **Documentación**: Se enriqueció con detalles técnicos y flujo completo

#### ¿Qué resultado se obtuvo?
- **Performance perfecta**: Todas las métricas alcanzaron 1.0000
- **ROC-AUC**: 1.0000 indica discriminación perfecta
- **Dos modelos entrenados**: Regresión Logística y Random Forest

#### Interpretación
El resultado perfecto (1.0 en todas las métricas) se debe al dataset pequeño y simplificado de 16 registros. En un escenario real con más datos, esperaría métricas más realistas (0.7-0.9). Los cambios en hiperparámetros muestran cómo diferentes configuraciones pueden afectar el rendimiento del modelo.

### Archivos modificados
1. `src/entrenar_modelo.py` - Hiperparámetros y Random Forest
2. `src/evaluar_modelo.py` - Métrica ROC-AUC
3. `README.md` - Documentación técnica extendida

### Comando para evidencia Git
```bash
git log --oneline --graph --all --decorate
```