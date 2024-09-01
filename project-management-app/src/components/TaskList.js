import React, { useEffect, useState } from 'react';
import { getTasks } from '../services/api';

function TaskList() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    getTasks().then(response => setTasks(response.data));
  }, []);

  return (
    <div>
      <h2>Tareas</h2>
      <ul>
        {tasks.map(task => (
          <li key={task.id}>{task.titulo}: {task.descripcion}</li>
        ))}
      </ul>
    </div>
  );
}

export default TaskList;
