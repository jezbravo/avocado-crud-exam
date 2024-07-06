from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from models import Task
from bson import ObjectId
import os


def database():
    mongo_url = os.getenv("MONGODB_URL", "mongodb://mongo:27017/task_database")
    # return AsyncIOMotorClient("mongodb://localhost:27017").task_database <- para uso local
    return AsyncIOMotorClient(mongo_url).task_database


# Obtener lista de tareas
async def get_all_tasks(db):
    all_tasks = []
    cursor = db.tasks.find({})
    async for document in cursor:
        all_tasks.append(Task(**document))
    return all_tasks


# Obtener una tarea por ID
async def get_task_by_id(db, id):
    task = await db.tasks.find_one({"_id": ObjectId(id)})
    if task:
        return task
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID: {id} not found",
        )


# Obtener una tarea por título
async def get_task_by_title(db, title):
    task = await db.tasks.find_one({"title": title})
    return task


# Crear tarea
async def create_task(db, task):
    new_task = await db.tasks.insert_one(task)
    created_task = await db.tasks.find_one({"_id": new_task.inserted_id})
    return created_task


# Actualizar tarea
async def update_task(db, id: str, data):
    # Actualizar los datos que sí se están recibiendo
    task = {key: value for key, value in data.dict().items() if value is not None}
    await db.tasks.update_one({"_id": ObjectId(id)}, {"$set": task})
    updated_task = await db.tasks.find_one({"_id": ObjectId(id)})
    return updated_task


# Eliminar tarea
async def delete_task(db, id: str):
    result = await db.tasks.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID: {id} not found",
        )
    else:
        return True
