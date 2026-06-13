"""
PRUEBAS COMPLETAS DE API - Casos válidos e inválidos
Actividad: API predictiva personalizada
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_endpoints_basicos():
    """Prueba de endpoints básicos"""
    print("=== PRUEBAS DE ENDPOINTS BÁSICOS ===")
    
    # GET /
    response = requests.get(f"{BASE_URL}/")
    print(f"GET /: {response.status_code} - {response.json()}")
    assert response.status_code == 200
    
    # GET /health
    response = requests.get(f"{BASE_URL}/health")
    print(f"GET /health: {response.status_code} - {response.json()}")
    assert response.status_code == 200
    
    # GET /info (mejora técnica)
    response = requests.get(f"{BASE_URL}/info")
    print(f"GET /info: {response.status_code} - {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200

def test_caso_valido():
    """Prueba con solicitud válida"""
    print("\n=== PRUEBA DE CASO VÁLIDO ===")
    
    datos_validos = {
        "edad": 35,
        "antiguedad_meses": 24,
        "saldo_promedio": 50000,
        "reclamos": 1,
        "usa_app": 1
    }
    
    response = requests.post(f"{BASE_URL}/predict", json=datos_validos)
    print(f"Caso válido: {response.status_code}")
    print(f"Respuesta: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    
    # Verificar campos adicionales de la mejora
    respuesta = response.json()
    assert "nivel_riesgo" in respuesta
    assert "descripcion" in respuesta
    assert "recomendacion" in respuesta
    assert "autor" in respuesta

def test_campo_faltante():
    """Prueba con campo faltante"""
    print("\n=== PRUEBA DE CAMPO FALTANTE ===")
    
    datos_incompletos = {
        "edad": 35,
        "antiguedad_meses": 24,
        "saldo_promedio": 50000
        # Faltan: reclamos, usa_app
    }
    
    response = requests.post(f"{BASE_URL}/predict", json=datos_incompletos)
    print(f"Campo faltante: {response.status_code}")
    print(f"Respuesta: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 422  # Validation error

def test_tipo_dato_incorrecto():
    """Prueba con tipo de dato incorrecto"""
    print("\n=== PRUEBA DE TIPO DE DATO INCORRECTO ===")
    
    datos_tipo_erroneo = {
        "edad": "treinta",  # Debe ser int
        "antiguedad_meses": 24,
        "saldo_promedio": 50000,
        "reclamos": 1,
        "usa_app": 1
    }
    
    response = requests.post(f"{BASE_URL}/predict", json=datos_tipo_erroneo)
    print(f"Tipo incorrecto: {response.status_code}")
    print(f"Respuesta: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 422  # Validation error

def test_valor_fuera_de_rango():
    """Prueba con valor fuera de rango"""
    print("\n=== PRUEBA DE VALOR FUERA DE RANGO ===")
    
    # Prueba 1: Edad fuera de rango
    datos_edad_invalida = {
        "edad": 150,  # Fuera del rango 18-100
        "antiguedad_meses": 24,
        "saldo_promedio": 50000,
        "reclamos": 1,
        "usa_app": 1
    }
    
    response = requests.post(f"{BASE_URL}/predict", json=datos_edad_invalida)
    print(f"Edad fuera de rango: {response.status_code}")
    print(f"Respuesta: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 422
    
    # Prueba 2: Saldo fuera de rango
    datos_saldo_invalido = {
        "edad": 35,
        "antiguedad_meses": 24,
        "saldo_promedio": 2000000,  # Mayor a $1,000,000
        "reclamos": 1,
        "usa_app": 1
    }
    
    response = requests.post(f"{BASE_URL}/predict", json=datos_saldo_invalido)
    print(f"Saldo fuera de rango: {response.status_code}")
    print(f"Respuesta: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 422

def test_valores_negativos():
    """Prueba con valores negativos"""
    print("\n=== PRUEBA DE VALORES NEGATIVOS ===")
    
    datos_negativos = {
        "edad": -5,  # No puede ser negativo
        "antiguedad_meses": -10,  # No puede ser negativo
        "saldo_promedio": -1000,  # No puede ser negativo
        "reclamos": 1,
        "usa_app": 1
    }
    
    response = requests.post(f"{BASE_URL}/predict", json=datos_negativos)
    print(f"Valores negativos: {response.status_code}")
    print(f"Respuesta: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 422

def test_varios_casos_validos():
    """Prueba con múltiples casos válidos para verificar niveles de riesgo"""
    print("\n=== PRUEBA DE MÚLTIPLES CASOS VÁLIDOS ===")
    
    casos = [
        {
            "nombre": "Cliente joven, bajo saldo",
            "datos": {
                "edad": 22,
                "antiguedad_meses": 6,
                "saldo_promedio": 5000,
                "reclamos": 0,
                "usa_app": 1
            }
        },
        {
            "nombre": "Cliente maduro, alto saldo",
            "datos": {
                "edad": 45,
                "antiguedad_meses": 60,
                "saldo_promedio": 150000,
                "reclamos": 2,
                "usa_app": 1
            }
        },
        {
            "nombre": "Cliente senior, muchos reclamos",
            "datos": {
                "edad": 65,
                "antiguedad_meses": 120,
                "saldo_promedio": 80000,
                "reclamos": 5,
                "usa_app": 0
            }
        }
    ]
    
    for caso in casos:
        response = requests.post(f"{BASE_URL}/predict", json=caso["datos"])
        print(f"\n{caso['nombre']}: {response.status_code}")
        print(f"Respuesta: {json.dumps(response.json(), indent=2)}")
        assert response.status_code == 200

if __name__ == "__main__":
    print("🚀 INICIANDO PRUEBAS COMPLETAS DE API")
    print("=" * 50)
    
    try:
        test_endpoints_basicos()
        test_caso_valido()
        test_campo_faltante()
        test_tipo_dato_incorrecto()
        test_valor_fuera_de_rango()
        test_valores_negativos()
        test_varios_casos_validos()
        
        print("\n" + "=" * 50)
        print("✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("✅ API lista para producción")
        
    except Exception as e:
        print(f"\n❌ ERROR EN PRUEBAS: {e}")
        print("Asegúrate de que la API esté corriendo en http://localhost:8000")
