# API RESTful CRUD

## Descripción

Esta es una aplicación de gestión de tareas: permite crear, editar, consultar y eliminar tareas.

### Stack

-FastAPI
-MongoDB
-React JS
-TailwindCSS

## Configuración

Clonar el repositorio:

```sh
git clone https://github.com/jezbravo/avocado-crud-exam.git
cd avocado-crud-exam
```

Instalar las dependencias:

### /backend

```sh
poetry install
```

### /frontend

```sh
npm install
```

## Variables de entorno:

### /backend

```sh
MONGODB_URI=mongodb://mongo:27017/task_database
FRONTEND_URL=http://localhost:5173
```

### /frontend

```sh
VITE_BACKEND_URL=http://localhost:8000
```

## Base de datos

Para el desarrollo de esta aplicación se utilizó una base de datos local.

```sh
mongod
```

## Iniciando el proyecto:

### /backend

```sh
uvicorn main:app --reload
```

### /frontend

```sh
npm run dev
```

## NOTA:

El comando `docker-compose up --build` todavía no funciona correctamente debido a problemas de configuración en la aplicación. Me encuentro trabajando para resolver este inconveniente a la brevedad. Favor de disculpar las molestias.
