from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Тестовая задача",
            "completed": False
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Тестовая задача"
    assert data["completed"] is False
    assert "id" in data


def test_update_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Задача для изменения",
            "completed": False
        }
    )

    task_id = create_response.json()["id"]

    response = client.patch(
        f"/tasks/{task_id}",
        json={
            "title": "Изменённая задача",
            "completed": True
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Изменённая задача"
    assert data["completed"] is True


def test_delete_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Задача для удаления",
            "completed": False
        }
    )

    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Задача удалена"