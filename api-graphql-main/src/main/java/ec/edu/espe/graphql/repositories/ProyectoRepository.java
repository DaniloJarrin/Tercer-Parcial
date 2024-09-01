package ec.edu.espe.graphql.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import ec.edu.espe.graphql.entities.Proyecto;

public interface ProyectoRepository extends JpaRepository<Proyecto, Long> {
}
