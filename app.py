from flask import Flask, request, jsonify  
from flask_sqlalchemy import SQLAlchemy     

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5433/tareasdb_utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

print("Cadena URI:", repr(app.config['SQLALCHEMY_DATABASE_URI']))
db = SQLAlchemy(app)

class Tarea(db.Model):
    __tablename__ = 'tareas' 
    id = db.Column(db.Integer, primary_key=True) 
    nombre = db.Column(db.String(200), nullable=False) 
    hecha = db.Column(db.Boolean, default=False)     

@app.before_request
def crear_tablas():
    db.create_all()

@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    tareas = Tarea.query.all() 
    return jsonify([    
        {'id': t.id, 'nombre': t.nombre, 'hecha': t.hecha} for t in tareas
    ])

@app.route('/tareas', methods=['POST'])
def crear_tarea():
    datos = request.json                      
    nueva = Tarea(nombre=datos['nombre'])     
    db.session.add(nueva)                      
    db.session.commit()                       
    return jsonify({'mensaje': 'Tarea creada'}), 201  

@app.route('/tareas/<int:id>', methods=['GET'])
def obtener_tarea(id):
    tarea = Tarea.query.get(id)
    if tarea:
        return jsonify({'id': tarea.id, 'nombre': tarea.nombre, 'hecha': tarea.hecha})
    return jsonify({'error': 'No encontrada'}), 404

@app.route('/tareas/<int:id>', methods=['PUT'])
def actualizar_tarea(id):
    tarea = Tarea.query.get(id)
    if tarea:
        datos = request.json
        tarea.nombre = datos.get('nombre', tarea.nombre) 
        tarea.hecha = datos.get('hecha', tarea.hecha)
        db.session.commit()
        return jsonify({'mensaje': 'Tarea actualizada'})
    return jsonify({'error': 'No encontrada'}), 404
 
@app.route('/tareas/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    tarea = Tarea.query.get(id)
    if tarea:
        db.session.delete(tarea)
        db.session.commit()
        return jsonify({'mensaje': 'Tarea eliminada'})
    return jsonify({'error': 'No encontrada'}), 404

# Ruta para obtener solo las tareas completadas
@app.route('/tareas/completadas', methods=['GET'])
def tareas_completadas():
    tareas = Tarea.query.filter_by(hecha=True).all()
    if not tareas:
        return jsonify({'error': 'No hay tareas completadas'}), 404
    return jsonify([
        {'id': t.id, 'nombre': t.nombre, 'hecha': t.hecha} for t in tareas
    ])
    
#Ruta para obtener solo las tares pendientes
@app.route('/tareas/pendientes', methods=['GET'])
def tareas_pendientes():
    tareas = Tarea.query.filter_by(hecha=False).all()
    if not tareas:
        return jsonify({'error': 'No hay tareas pendientes'}), 404
    return jsonify([
        {'id': t.id, 'nombre': t.nombre, 'hecha': t.hecha} for t in tareas
    ])
    
#Ruta para filtrar las tareas por su nombre
@app.route('/tareas/buscar/<palabra>', methods=['GET'])
def buscar_tareas(palabra):
    # Buscar tareas cuyo nombre contenga la palabra (sin distinguir mayúsculas/minúsculas)
    tareas = Tarea.query.filter(Tarea.nombre.ilike(f'%{palabra}%')).all()
    
    if not tareas:
        return jsonify({'error': f'No se encontraron tareas que contengan "{palabra}"'}), 404

    return jsonify([
        {'id': t.id, 'nombre': t.nombre, 'hecha': t.hecha} for t in tareas
    ])

@app.route('/')
def index():
    return jsonify({"mensaje": "Bienvenido a la API de tareas. Usa /tareas para ver las tareas."})

if __name__ == '__main__':
    app.run(debug=True)