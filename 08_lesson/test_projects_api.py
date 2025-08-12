import uuid
import requests

from config import BASE_URL, HEADERS


def generate_unique_name():
    return f"Test Project {uuid.uuid4()}"


def test_create_project_positive():
    unique_project_name = generate_unique_name()
    response = requests.post(
        f"{BASE_URL}/projects",
        headers=HEADERS,
        json={"name": unique_project_name},
    )
    assert response.status_code == 201, "Проект не создан"
    project_id = response.json().get("id")
    assert project_id is not None, "В ответе нет id проекта"

    get_resp = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS,
    )
    assert get_resp.status_code == 200, "Не удалось получить проект"
    data = get_resp.json()
    assert data.get("name") == unique_project_name, (
        "Название проекта не совпадает"
    )


def test_get_project_positive():
    create_resp = requests.post(
        f"{BASE_URL}/projects",
        headers=HEADERS,
        json={"name": "Temporary Project"},
    )
    assert create_resp.status_code == 201, "Проект для теста не создан"
    project_id = create_resp.json().get("id")
    assert project_id is not None, "В ответе нет id проекта"

    get_resp = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS,
    )
    assert get_resp.status_code == 200, "Не удалось получить проект"
    assert get_resp.json().get("id") == project_id, "ID не совпадает"


def test_update_project_positive():
    create_resp = requests.post(
        f"{BASE_URL}/projects",
        headers=HEADERS,
        json={"name": "Old Name"},
    )
    assert create_resp.status_code == 201, "Проект для обновления не создан"
    project_id = create_resp.json().get("id")
    assert project_id is not None, "В ответе нет id проекта"

    update_resp = requests.put(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS,
        json={"name": "Updated Project"},
    )
    assert update_resp.status_code == 200, "Проект не обновлён"

    get_resp = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS,
    )
    assert get_resp.status_code == 200, "Не удалось получить проект"
    assert get_resp.json().get("name") == "Updated Project", (
        "Название проекта не обновилось"
    )


def test_create_project_without_name():
    response = requests.post(
        f"{BASE_URL}/projects",
        headers=HEADERS,
        json={},
    )
    assert response.status_code == 400, (
        "Ожидался 400 при создании без имени"
    )


def test_get_project_invalid_id():
    response = requests.get(
        f"{BASE_URL}/projects/invalid-id",
        headers=HEADERS,
    )
    assert response.status_code == 404, (
        "Ожидался 404 для несуществующего проекта"
    )


def test_update_project_invalid_id():
    response = requests.put(
        f"{BASE_URL}/projects/invalid-id",
        headers=HEADERS,
        json={"name": "New Name"},
    )
    assert response.status_code == 404, (
        "Ожидался 404 при обновлении несуществующего проекта"
    )
