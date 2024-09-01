import React from 'react';
import ProjectList from './components/ProjectList';
import TaskForm from './components/TaskForm';
import EmployeeList from './components/EmployeeList';

function App() {
  return (
    <div className="App">
      <h1>Gestión de Proyectos</h1>
      <ProjectList />
      <h1>Gestión de Empleados</h1>
      <EmployeeList />
      <h1>Gestión de Tareas</h1>
      <TaskForm />
    </div>
  );
}

export default App;
