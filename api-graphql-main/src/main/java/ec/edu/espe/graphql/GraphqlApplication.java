package ec.edu.espe.graphql;

import ec.edu.espe.graphql.entities.Proyecto;
import ec.edu.espe.graphql.entities.Tarea;
import ec.edu.espe.graphql.entities.Empleado;
import ec.edu.espe.graphql.repositories.ProyectoRepository;
import ec.edu.espe.graphql.repositories.TareaRepository;
import ec.edu.espe.graphql.repositories.EmpleadoRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import java.util.List;
import java.util.Random;

@SpringBootApplication
public class GraphqlApplication {

    Random random = new Random();

    public static void main(String[] args) {
        SpringApplication.run(GraphqlApplication.class, args);
    }

    @Bean
    CommandLineRunner commandLineRunner(ProyectoRepository proyectoRepository, TareaRepository tareaRepository, EmpleadoRepository empleadoRepository) {
        return args -> {
            List.of("Proyecto A", "Proyecto B", "Proyecto C").forEach(proy -> {
                Proyecto proyecto = new Proyecto();
                proyecto.setNombre(proy);
                proyecto.setDescripcion(proy + " descripción");
                proyectoRepository.save(proyecto);
            });

            List.of("Empleado A", "Empleado B", "Empleado C").forEach(emp -> {
                Empleado empleado = new Empleado();
                empleado.setNombre(emp);
                empleado.setPuesto(emp + " puesto");
                empleadoRepository.save(empleado);
            });
        };
    }
}
