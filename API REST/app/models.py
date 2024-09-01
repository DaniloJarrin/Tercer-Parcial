from . import db

# Modelo de Proyecto
class Proyecto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200), nullable=True)
    tareas = db.relationship('Tarea', backref='proyecto', lazy=True)

# Modelo de Empleado
class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    puesto = db.Column(db.String(100), nullable=False)
    tareas = db.relationship('Tarea', secondary='tarea_empleado', back_populates='empleados')

# Modelo de Tarea
class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200), nullable=True)
    proyecto_id = db.Column(db.Integer, db.ForeignKey('proyecto.id'), nullable=False)
    empleados = db.relationship('Empleado', secondary='tarea_empleado', back_populates='tareas')

# Tabla de asociación para la relación muchos a muchos entre Tarea y Empleado
tarea_empleado = db.Table('tarea_empleado',
    db.Column('tarea_id', db.Integer, db.ForeignKey('tarea.id'), primary_key=True),
    db.Column('empleado_id', db.Integer, db.ForeignKey('empleado.id'), primary_key=True)
)
