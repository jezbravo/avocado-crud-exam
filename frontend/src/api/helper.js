import axios from "axios";

const URL = "http://localhost:8000";
const endpoint = `${URL}/tasks`;

// Obtener una tarea
export const getTask = (id) => {
  return axios.get(`${endpoint}/${id}`);
};

// Obtener todas las tareas
export const getAllTasks = () => {
  return axios.get(endpoint);
};

// Crear tarea
export const createTask = (newTask) => {
  return axios.post(endpoint, newTask);
};

// Actualizar tarea
export const updateTask = (id, task) => {
  return axios.put(`${endpoint}/${id}`, task);
};

// Eliminar tarea
export const deleteTask = (id) => {
  return axios.delete(`${endpoint}/${id}`);
};
