from fastapi import FastAPI
from routes.task import router
from fastapi.middleware.cors import CORSMiddleware
from decouple import config


app = FastAPI(
    title="API de Ezequiel Bravo",
    description="Examen API RESTful en donde se desarrolla una aplicación de gestión de tareas",
    version="1.0.0",
)

origins = config("FRONTEND_URL")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def welcome():
    return {"message": "API RESTfull Home Page"}


app.include_router(router)
