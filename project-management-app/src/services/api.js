import axios from 'axios';

// Configurar la URL base de la API REST
const restAPI = axios.create({
  baseURL: 'http://localhost:5000', // Cambia el puerto si es necesario
});

// Configurar la URL base de la API GraphQL
const graphqlAPI = axios.create({
  baseURL: 'http://127.0.0.1:8000/graphql',
});

// Funciones para interactuar con la API REST para Tareas
export const getTasks = () => restAPI.get('/tareas');
export const createTask = (task) => restAPI.post('/tareas', task);
export const updateTask = (id, task) => restAPI.put(`/tareas/${id}`, task);
export const deleteTask = (id) => restAPI.delete(`/tareas/${id}`);

// Funciones para interactuar con la API GraphQL para Proyectos y Empleados
export const getProjects = () => 
  graphqlAPI.post('', { query: '{ proyectos { id nombre descripcion } }' });

export const getEmployees = () => 
  graphqlAPI.post('', { query: '{ empleados { id nombre puesto } }' });

export const createProject = (nombre, descripcion) =>
  graphqlAPI.post('', {
    query: `
      mutation {
        createProyecto(nombre: "${nombre}", descripcion: "${descripcion}") {
          id
          nombre
          descripcion
        }
      }
    `,
  });

export const createEmployee = (nombre, puesto) =>
  graphqlAPI.post('', {
    query: `
      mutation {
        createEmpleado(nombre: "${nombre}", puesto: "${puesto}") {
          id
          nombre
          puesto
        }
      }
    `,
  });
