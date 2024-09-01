from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Importa Flask-CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configura la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5433/task_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Configura CORS
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})  # Esto permite solicitudes desde localhost:3000

    db.init_app(app)
    
    with app.app_context():
        # Importa y registra el Blueprint de rutas
        from . import routes
        app.register_blueprint(routes.main)
        
        # Crea las tablas en la base de datos si no existen
        db.create_all()

    return app
