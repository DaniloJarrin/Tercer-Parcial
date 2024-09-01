from flask import Blueprint, request, jsonify
from . import db
from .models import Proyecto, Empleado, Tarea

main = Blueprint('main', __name__)

# Rutas para Proyectos

@main.route('/proyectos', methods=['POST'])
def create_proyecto():
    data = request.json
    new_proyecto = Proyecto(nombre=data['nombre'], descripcion=data['descripcion'])
    db.session.add(new_proyecto)
    db.session.commit()
    return jsonify({"mensaje": "Proyecto creado con éxito"}), 201

@main.route('/proyectos', methods=['GET'])
def get_proyectos():
    proyectos = Proyecto.query.all()
    output = [{"id": proyecto.id, "nombre": proyecto.nombre, "descripcion": proyecto.descripcion} for proyecto in proyectos]
    return jsonify(output), 200

@main.route('/proyectos/<int:id>', methods=['PUT'])
def update_proyecto(id):
    data = request.json
    proyecto = Proyecto.query.get(id)
    if not proyecto:
        return jsonify({"mensaje": "Proyecto no encontrado"}), 404
    proyecto.nombre = data['nombre']
    proyecto.descripcion = data['descripcion']
    db.session.commit()
    return jsonify({"mensaje": "Proyecto actualizado con éxito"}), 200

@main.route('/proyectos/<int:id>', methods=['DELETE'])
def delete_proyecto(id):
    proyecto = Proyecto.query.get(id)
    if not proyecto:
        return jsonify({"mensaje": "Proyecto no encontrado"}), 404
    db.session.delete(proyecto)
    db.session.commit()
    return jsonify({"mensaje": "Proyecto eliminado con éxito"}), 200

# Rutas para Empleados

@main.route('/empleados', methods=['POST'])
def create_empleado():
    data = request.json
    new_empleado = Empleado(nombre=data['nombre'], puesto=data['puesto'])
    db.session.add(new_empleado)
    db.session.commit()
    return jsonify({"mensaje": "Empleado creado con éxito"}), 201

@main.route('/empleados', methods=['GET'])
def get_empleados():
    empleados = Empleado.query.all()
    output = [{"id": empleado.id, "nombre": empleado.nombre, "puesto": empleado.puesto} for empleado in empleados]
    return jsonify(output), 200

@main.route('/empleados/<int:id>', methods=['PUT'])
def update_empleado(id):
    data = request.json
    empleado = Empleado.query.get(id)
    if not empleado:
        return jsonify({"mensaje": "Empleado no encontrado"}), 404
    empleado.nombre = data['nombre']
    empleado.puesto = data['puesto']
    db.session.commit()
    return jsonify({"mensaje": "Empleado actualizado con éxito"}), 200

@main.route('/empleados/<int:id>', methods=['DELETE'])
def delete_empleado(id):
    empleado = Empleado.query.get(id)
    if not empleado:
        return jsonify({"mensaje": "Empleado no encontrado"}), 404
    db.session.delete(empleado)
    db.session.commit()
    return jsonify({"mensaje": "Empleado eliminado con éxito"}), 200

# Rutas para Tareas

@main.route('/tareas', methods=['POST'])
def create_tarea():
    data = request.json
    new_tarea = Tarea(titulo=data['titulo'], descripcion=data['descripcion'], proyecto_id=data['proyectoId'])
    for empleado_id in data['empleadoIds']:
        empleado = Empleado.query.get(empleado_id)
        if empleado:
            new_tarea.empleados.append(empleado)
    db.session.add(new_tarea)
    db.session.commit()
    return jsonify({"mensaje": "Tarea creada con éxito"}), 201

@main.route('/tareas', methods=['GET'])
def get_tareas():
    tareas = Tarea.query.all()
    output = [{"id": tarea.id, "titulo": tarea.titulo, "descripcion": tarea.descripcion, "proyecto_id": tarea.proyecto_id,
               "empleados": [{"id": emp.id, "nombre": emp.nombre} for emp in tarea.empleados]} for tarea in tareas]
    return jsonify(output), 200

@main.route('/tareas/<int:id>', methods=['PUT'])
def update_tarea(id):
    data = request.json
    tarea = Tarea.query.get(id)
    if not tarea:
        return jsonify({"mensaje": "Tarea no encontrada"}), 404
    tarea.titulo = data['titulo']
    tarea.descripcion = data['descripcion']
    tarea.proyecto_id = data['proyectoId']
    tarea.empleados = []
    for empleado_id in data['empleadoIds']:
        empleado = Empleado.query.get(empleado_id)
        if empleado:
            tarea.empleados.append(empleado)
    db.session.commit()
    return jsonify({"mensaje": "Tarea actualizada con éxito"}), 200

@main.route('/tareas/<int:id>', methods=['DELETE'])
def delete_tarea(id):
    tarea = Tarea.query.get(id)
    if not tarea:
        return jsonify({"mensaje": "Tarea no encontrada"}), 404
    db.session.delete(tarea)
    db.session.commit()
    return jsonify({"mensaje": "Tarea eliminada con éxito"}), 200
