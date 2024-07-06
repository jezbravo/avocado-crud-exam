# API RESTful CRUD

## Descripción

Esta es una aplicación de gestión de tareas: permite crear, editar, consultar y eliminar tareas.

### Stack

- FastAPI
- MongoDB
- React JS
- TailwindCSS

## Configuración

Clonar el repositorio:

```sh
git clone https://github.com/jezbravo/avocado-crud-exam.git
cd avocado-crud-exam
```

## Configurar las variables de entorno:

### /backend/.env:

```sh
MONGODB_URL=mongodb://mongo:27017/task_database
FRONTEND_URL=http://localhost:5173
```

### /frontend/.env:

```sh
VITE_BACKEND_URL=http://localhost:8000
```

## Iniciar el proyecto:

```sh
docker-compose up
```

## URLs de acceso:

### Backend:

(http://localhost:8000)

### Frontend:

(http://localhost:5173)
