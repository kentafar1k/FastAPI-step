from fastapi.testclient import TestClient
import pytest

def test_register_user(client):
    # Тест успешной регистрации
    response = client.post(
        "/register",
        json={"username": "testuser", "password": "testpass"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully!"}

def test_register_duplicate_user(client):
    # Регистрируем пользователя первый раз
    client.post(
        "/register",
        json={"username": "duplicate", "password": "testpass"}
    )
    
    # Пытаемся зарегистрировать того же пользователя
    response = client.post(
        "/register",
        json={"username": "duplicate", "password": "testpass"}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Username already registered"}

def test_register_invalid_data(client):
    # Тест с неполными данными
    response = client.post(
        "/register",
        json={"username": "testuser"}  # Отсутствует пароль
    )
    assert response.status_code == 422  # Ошибка валидации