from fastapi import APIRouter, Depends, HTTPException, status

from database import (
    database,
    get_all_tasks,
    create_task,
    get_task_by_title,
    get_task_by_id,
    delete_task,
    update_task,
)

from models import Task, UpdateTask

router = APIRouter(prefix="/tasks", tags=["tasks"])


# Obtener lista de tareas
@router.get("/")
async def get_tasks(db=Depends(database)):
    all_tasks = await get_all_tasks(db)
    return all_tasks


# Obtener una tarea
@router.get("/{id}", response_model=Task)
async def get_single_task(id: str, db=Depends(database)):
    task = await get_task_by_id(db, id)
    if task:
        return task
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID: {id} not found",
        )


# Crear tarea
@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def new_task(task: Task, db=Depends(database)):
    # Comprobar que la tarea no esté duplicada
    found_task = await get_task_by_title(db, task.title)
    if found_task:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Task already exists"
        )

    response = await create_task(db, task.model_dump())
    if response:
        return response
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Creation error"
        )


# Actualizar tarea
@router.put("/{id}", response_model=Task, status_code=status.HTTP_200_OK)
async def edit_task(id: str, task: UpdateTask, db=Depends(database)):
    response = await update_task(db, id, task)
    if response:
        return response
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID: {id} not found",
        )


# Eliminar tarea
@router.delete("/{id}")
async def remove_task(id: str, db=Depends(database)):
    response = await delete_task(db, id)
    if response:
        return f"Task with ID: {id} deleted successfully"
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID: {id} not found",
        )
