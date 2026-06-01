"""
NUEVA PRUEBA DE API - Usando requests
"""
import requests

BASE_URL = "http://localhost:8000"

def test_health():
    response = requests.get(f"{BASE_URL}/health")
    print(f"Health: {response.status_code} - {response.json()}")
    assert response.status_code == 200

def test_predict():
    datos = {"edad": 35, "antiguedad_meses": 24, "saldo_promedio": 50000, "reclamos": 1, "usa_app": 1}
    response = requests.post(f"{BASE_URL}/predict", json=datos)
    print(f"Predicción: {response.status_code} - {response.json()}")
    assert response.status_code == 200

if __name__ == "__main__":
    print("\n=== NUEVA PRUEBA DE API ===\n")
    test_health()
    test_predict()
    print("\n✅ Prueba completada")