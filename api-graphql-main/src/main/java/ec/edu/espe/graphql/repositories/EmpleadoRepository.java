package ec.edu.espe.graphql.repositories;
import org.springframework.data.jpa.repository.JpaRepository;

import ec.edu.espe.graphql.entities.Empleado;
public interface EmpleadoRepository extends JpaRepository<Empleado, Long> {
}
