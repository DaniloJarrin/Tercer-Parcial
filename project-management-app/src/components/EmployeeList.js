import React, { useState, useEffect } from 'react';
import axios from 'axios';

function EmployeeList() {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/empleados')
      .then(response => {
        setEmployees(response.data);
        setLoading(false);
      })
      .catch(error => {
        setError("Error al cargar empleados");
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Cargando empleados...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <ul>
        {employees.map(employee => (
          <li key={employee.id}>{employee.nombre} - {employee.puesto}</li>
        ))}
      </ul>
    </div>
  );
}

export default EmployeeList;
