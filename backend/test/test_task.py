import pytest
import random
import json
from fastapi import status
from main import app
from bson import ObjectId
from httpx import AsyncClient, ASGITransport


# Cliente asíncrono
@pytest.fixture
async def async_client():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000"
    ) as client:
        yield client


# Obtener lista de tareas
@pytest.mark.asyncio
# Crear la tarea para su obtención
async def test_get_tasks(async_client):
    payload = {
        "title": "tarea 0",
        "description": "CRUD en FastAPI",
        "completed": True,
    }
    json_data = json.loads(json.dumps(payload))
    await async_client.post("/tasks/", json=json_data)

    # Obtener tareas
    response = await async_client.get("/tasks/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() != []


# Obtener una tarea mediante ID
@pytest.mark.asyncio
async def test_get_single_task(async_client):
    tasks = await async_client.get("/tasks/")
    all_tasks = tasks.json()
    valid_id = all_tasks[0]["_id"]
    title = all_tasks[0]["title"]
    description = all_tasks[0]["description"]
    completed = all_tasks[0]["completed"]
    response = await async_client.get(f"/tasks/{valid_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "_id": valid_id,
        "title": title,
        "description": description,
        "completed": completed,
    }


# Buscar una tarea mediante un ID inválido
@pytest.mark.asyncio
async def test_get_single_task_wrong_id(async_client):
    invalid_id = "667cd4d0b5c638a43d37f93e"
    response = await async_client.get(f"/tasks/{invalid_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": f"Task with ID: {invalid_id} not found"}


# Crear tarea
@pytest.mark.asyncio
async def test_new_task(async_client):
    task = random.randint(1, 1000)
    payload = {"title": f"test task n° {task}"}
    json_data = json.loads(json.dumps(payload))
    response = await async_client.post("/tasks/", json=json_data)
    assert response.status_code == status.HTTP_201_CREATED, response.text
    response_data = response.json()
    task_id = response_data.get("_id")
    assert task_id is not None
    assert ObjectId.is_valid(task_id)
    assert response_data == {
        "_id": task_id,
        "title": f"test task n° {task}",
        "description": None,
        "completed": False,
    }


# Comprobar que la tarea existe
@pytest.mark.asyncio
async def test_task_exists(async_client):
    payload = {"title": "tarea 0"}
    json_data = json.loads(json.dumps(payload))
    response = await async_client.post("/tasks/", json=json_data)
    assert response.status_code == status.HTTP_409_CONFLICT
    assert response.json() == {"detail": "Task already exists"}


# Actualizar una tarea
@pytest.mark.asyncio
async def test_edit_task(async_client):
    payload = {
        "title": "tarea -1",
        "description": "CRUD en FastAPI (updated)",
        "completed": False,
    }
    json_data = json.loads(json.dumps(payload))
    tasks = await async_client.get("/tasks/")
    all_tasks = tasks.json()
    valid_id = all_tasks[0]["_id"]
    response = await async_client.put(f"/tasks/{valid_id}", json=json_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "_id": valid_id,
        "title": "tarea -1",
        "description": "CRUD en FastAPI (updated)",
        "completed": False,
    }


# Actualizar una tarea inexistente
@pytest.mark.asyncio
async def test_edit_task_wrong_id(async_client):
    payload = {"title": "tarea inexistente"}
    json_data = json.loads(json.dumps(payload))
    invalid_id = "667cd4d0b5c638a43d37f93e"
    response = await async_client.put(f"/tasks/{invalid_id}", json=json_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": f"Task with ID: {invalid_id} not found"}


# Eliminar una tarea
@pytest.mark.asyncio
async def test_remove_task(async_client):
    # Crear la tarea a eliminar
    payload = {
        "title": "tarea para eliminar",
    }
    json_data = json.loads(json.dumps(payload))
    await async_client.post("/tasks/", json=json_data)
    tasks = await async_client.get("/tasks/")
    all_tasks = tasks.json()
    valid_id = all_tasks[-1]["_id"]

    # Eliminar la tarea
    response = await async_client.delete(f"/tasks/{valid_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == f"Task with ID: {valid_id} deleted successfully"


# Eliminar una tarea inexistente
@pytest.mark.asyncio
async def test_remove_task_wrong_id(async_client):
    invalid_id = "667cd4d0b5c638a43d37f93e"
    response = await async_client.delete(f"/tasks/{invalid_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": f"Task with ID: {invalid_id} not found"}
