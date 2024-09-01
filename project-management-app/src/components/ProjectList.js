import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ProjectList() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/proyectos')
      .then(response => {
        setProjects(response.data);
        setLoading(false);
      })
      .catch(error => {
        setError("Error al cargar proyectos");
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Cargando proyectos...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <ul>
        {projects.map(project => (
          <li key={project.id}>{project.nombre} - {project.descripcion}</li>
        ))}
      </ul>
    </div>
  );
}

export default ProjectList;
