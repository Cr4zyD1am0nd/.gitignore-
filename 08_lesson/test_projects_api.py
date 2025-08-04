import requests
import pytest
from config import BASE_URL, HEADERS


@pytest.fixture
def unique_project_name():
    import uuid
    return f"Test Project {uuid.uuid4()}"


def test_create_project_positive(unique_project_name):
    response = requests.post(
        f"{BASE_URL}/projects",
        headers=HEADERS,
        json={"name": unique_project_name}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == unique_project_name


def test_get_project_positive():
    # Сначала создаём проект
    create_resp = requests.post(
        f"{BASE_URL}/projects",
        headers=HEADERS,
        json={"name": "Temporary Project"}
    )
    assert create_resp.status_code == 200
    project_id = create_resp.json()["id"]

    # Получаем проект по ID
    get_resp = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS
    )
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == project_id


def test_update_project_positive():
    # Создаём проект
    create_resp = requests.post(
        f"{BASE_URL}/projects",
        headers=HEADERS,
        json={"name": "Old Name"}
    )
    assert create_resp.status_code == 200
    project_id = create_resp.json()["id"]

    # Обновляем имя проекта
    update_resp = requests.put(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS,
        json={"name": "Updated Project"}
    )
    assert update_resp.status_code == 200
    assert update_resp.json()["name"] == "Updated Project"


def test_create_project_without_name():
    response = requests.post(
        f"{BASE_URL}/projects",
        headers=HEADERS,
        json={}  # пропущено обязательное поле
    )
    assert response.status_code == 400


def test_get_project_invalid_id():
    response = requests.get(
        f"{BASE_URL}/projects/invalid-id",
        headers=HEADERS
    )
    assert response.status_code in [400, 404]


def test_update_project_invalid_id():
    response = requests.put(
        f"{BASE_URL}/projects/invalid-id",
        headers=HEADERS,
        json={"name": "New Name"}
    )
    assert response.status_code in [400, 404]
