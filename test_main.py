import pytest
from main import app, preprocess

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_predict(client):
    input_data = {
        "holiday": 0,
        "weekday": 6,
        "workingday": 0,
        "weathersit": 2,
        "temp": 0.344167,
        "atemp": 0.363625,
        "hum": 0.805833,
        "windspeed": 0.160446,
        "casual": 331,
        "registered": 654
    }
    response = client.post('/predict', json=input_data)
    print(response.status_code)
    print(response.json)
    assert response.status_code == 200
    assert response.json["predictions"][0] >= 0

def test_predict_failure(client):
    input_data = {
        "holiday": 0,
        "weekday": 6,
        "workingday": 0,
        "weathersit": 2,
        "temp": 0.344167,
        "atemp": 0.363625,
    }
    response = client.post('/predict', json=input_data)
    print(response.status_code)
    print(response.json)
    assert response.status_code == 400