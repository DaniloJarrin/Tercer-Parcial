import React, { useEffect, useState } from 'react';
import axios from 'axios';

const TaskForm = () => {
  const [taskTitle, setTaskTitle] = useState('');
  const [taskDescription, setTaskDescription] = useState('');
  const [proyectos, setProyectos] = useState([]);
  const [empleados, setEmpleados] = useState([]);
  const [selectedProyecto, setSelectedProyecto] = useState('');
  const [selectedEmpleados, setSelectedEmpleados] = useState([]);

  useEffect(() => {
    const fetchProyectos = async () => {
      try {
        const projectQuery = `
          {
            proyectos {
              id
              nombre
            }
          }
        `;
        const encodedProjectQuery = encodeURIComponent(projectQuery);
        const response = await axios.get(`http://localhost:8000/graphql?query=${encodedProjectQuery}`);
        setProyectos(response.data.data.proyectos);
      } catch (error) {
        console.error("Error al cargar proyectos", error);
      }
    };

    const fetchEmpleados = async () => {
      try {
        const employeeQuery = `
          {
            empleados {
              id
              nombre
            }
          }
        `;
        const encodedEmployeeQuery = encodeURIComponent(employeeQuery);
        const response = await axios.get(`http://localhost:8000/graphql?query=${encodedEmployeeQuery}`);
        setEmpleados(response.data.data.empleados);
      } catch (error) {
        console.error("Error al cargar empleados", error);
      }
    };

    fetchProyectos();
    fetchEmpleados();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const taskData = {
        titulo: taskTitle,
        descripcion: taskDescription,
        proyectoId: selectedProyecto,
        empleadoIds: selectedEmpleados,
      };
      const response = await axios.post('http://localhost:5000/tareas', taskData);
      console.log("Tarea creada", response.data);
    } catch (error) {
      console.error("Error al crear tarea", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Título de la Tarea:</label>
        <input type="text" value={taskTitle} onChange={e => setTaskTitle(e.target.value)} />
      </div>
      <div>
        <label>Descripción:</label>
        <textarea value={taskDescription} onChange={e => setTaskDescription(e.target.value)} />
      </div>
      <div>
        <label>Proyecto:</label>
        <select value={selectedProyecto} onChange={e => setSelectedProyecto(e.target.value)}>
          <option value="">Seleccione un proyecto</option>
          {proyectos.map(proj => (
            <option key={proj.id} value={proj.id}>{proj.nombre}</option>
          ))}
        </select>
      </div>
      <div>
        <label>Empleados:</label>
        <select multiple value={selectedEmpleados} onChange={e => setSelectedEmpleados(Array.from(e.target.selectedOptions, option => option.value))}>
          {empleados.map(emp => (
            <option key={emp.id} value={emp.id}>{emp.nombre}</option>
          ))}
        </select>
      </div>
      <button type="submit">Crear Tarea</button>
    </form>
  );
};

export default TaskForm;
