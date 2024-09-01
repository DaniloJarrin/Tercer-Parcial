package ec.edu.espe.graphql.repositories;
import org.springframework.data.jpa.repository.JpaRepository;
import ec.edu.espe.graphql.entities.Tarea;

public interface TareaRepository extends JpaRepository<Tarea, Long> {
 
}
