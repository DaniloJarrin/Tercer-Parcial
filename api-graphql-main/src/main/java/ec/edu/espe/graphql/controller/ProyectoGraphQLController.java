package ec.edu.espe.graphql.controller;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.MutationMapping;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import ec.edu.espe.graphql.repositories.EmpleadoRepository;
import ec.edu.espe.graphql.repositories.ProyectoRepository;
import ec.edu.espe.graphql.entities.Proyecto;
import ec.edu.espe.graphql.dto.*;
@Controller
public class ProyectoGraphQLController {
    
    @Autowired
    private ProyectoRepository proyectoRepository;

    @Autowired
    private EmpleadoRepository empleadoRepository;

    @QueryMapping
    public List<Proyecto> getProyectos() {
        return proyectoRepository.findAll();
    }

    @MutationMapping
    public Proyecto createProyecto(@Argument ProyectoRequest proyectoRequest) {
        Proyecto proyecto = new Proyecto();
        proyecto.setNombre(proyectoRequest.getNombre());
        proyecto.setDescripcion(proyectoRequest.getDescripcion());
        return proyectoRepository.save(proyecto);
    }

    @MutationMapping
    public Proyecto updateProyecto(@Argument Long id, @Argument ProyectoRequest proyectoRequest) {
        Proyecto proyecto = proyectoRepository.findById(id).orElseThrow(() -> new RuntimeException("Proyecto no encontrado"));
        proyecto.setNombre(proyectoRequest.getNombre());
        proyecto.setDescripcion(proyectoRequest.getDescripcion());
        return proyectoRepository.save(proyecto);
    }

    @MutationMapping
    public boolean deleteProyecto(@Argument Long id) {
        proyectoRepository.deleteById(id);
        return true;
    }
}
