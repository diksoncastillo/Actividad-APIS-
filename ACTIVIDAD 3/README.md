# API de Tareas - Flask + PostgreSQL

Este proyecto es una API RESTful para la gestión de tareas construida con Flask, SQLAlchemy y PostgreSQL. Permite crear, consultar, actualizar, eliminar, buscar y filtrar tareas, ademas de que es necesario tener instalado Postman para poder usar el programa de manera local. 

Usé un .venv llamado env.venv, es recomendable usar un ambiente virtual personalizado.

---
## Grupo de Trabajo

| Nombre Completo                 |    Código    |       
|---------------------------------|--------------|
| Dikson Javier Castillo Triviño  | 20232020115  |

---
## Estructura del Proyecto

```
PRACTICA 3/
├── app.py              # Código principal de la API
├── create_db.py        # Script opcional para crear la base de datos
├── requirements.txt    # Lista de dependencias
└── README.md           # Este archivo
```

---

## Requisitos Previos

1. Python 3.10 o superior
2. PostgreSQL instalado y en funcionamiento
3. Crear una base de datos, en este caso `tareasdb_utf8`
4. Tener `psycopg2`, `flask` y `flask_sqlalchemy` instalados
5. Tener Postman instalado y en funcionamiento 

> **Nota**: Si no tienes `requirements.txt`, puedes instalar los paquetes directamente:
"pip install flask flask_sqlalchemy psycopg2-binary"


---

##  Configuración de la Base de Datos

Verifica que el siguiente URI en `app.py` coincida con tus credenciales de PostgreSQL:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5433/tareasdb_utf8'
```
Tambien puedes tener el tuyo personalizado pero eso requeriría modificar mas partes del código, por lo cual no es recomendable.
---

##  Ejecución

Desde la terminal, ve a la carpeta del proyecto y ejecuta:

```bash
python app.py
```

Verás algo como:

```
* Running on http://127.0.0.1:5000
```

---

## Pruebas con Postman

Puedes probar cada ruta de la API usando Postman:

### 1. Obtener todas las tareas
- Método: `GET`
- URL: `http://localhost:5000/tareas`

### 2. Crear nueva tarea
- Método: `POST`
- URL: `http://localhost:5000/tareas`
- Body (JSON):
  ```json
  {
    "nombre": "Tarea Nueva"
  }
  ```

### 3. Obtener tarea por ID
- Método: `GET`
- URL: `http://localhost:5000/tareas/ID`

### 4. Actualizar tarea
- Método: `PUT`
- URL: `http://localhost:5000/tareas/ID`
- Body (JSON):
  ```json
  {
    "nombre": "Tarea 1",
    "hecha": true
  }
  ```

### 5. Eliminar tarea
- Método: `DELETE`
- URL: `http://localhost:5000/tareas/ID`

### 6. Ver tareas completadas
- Método: `GET`
- URL: `http://localhost:5000/tareas/completadas`

### 7. Buscar tareas por palabra clave
- Método: `GET`
- URL: `http://localhost:5000/tareas/buscar/palabra`

---

##  Funcionalidades Incluidas

- Crear nuevas tareas
- Ver todas las tareas
- Consultar tarea por ID
- Actualizar el nombre o estado de la tarea (`hecha`: `true/false`)
- Eliminar tarea
- Ver solo las tareas completadas
- Buscar tareas por nombre (sin distinguir mayúsculas/minúsculas)

---

##  Notas

- La base de datos se crea automáticamente si no existe al ejecutar la API, de igual manera en el GitHub se encuentra un archivo "crear_db.py" la cual ayuda a generar la base de datos de manera inmediata.
- Usa Postman para pruebas.
