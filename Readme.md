# Sistema de Gestión y Venta de Películas
Proyecto para la gestión y venta de películas con funcionalidades completas de inventario, usuarios y ventas.(desarrollo)

sistema_peliculas/
│
├── app/                         # Carpeta principal de la aplicación Flask
│   ├── __init__/                # Inicialización del proyecto Flask
│   │   ├── __init__.py          # Configuración de la aplicación y base de datos
│   │   ├── config.py            # Configuración global del proyecto
│   │
│   ├── routes/                  # Controladores (endpoints API/CRUD)
│   │   ├── __init__.py          # Importación de rutas
│   │   ├── generos_routes.py    # CRUD para "Generos"
│   │   ├── roles_routes.py      # CRUD para "Roles"
│   │   ├── usuarios_routes.py   # CRUD para "Usuarios"
│   │   ├── peliculas_routes.py  # CRUD para "Peliculas"
│   │   ├── compras_routes.py    # CRUD para "Compras"
│   │
│   ├── models/                  # Modelos de base de datos (ORM)
│   │   ├── __init__.py          # Configuración de SQLAlchemy
│   │   ├── genero.py            # Modelo "Generos"
│   │   ├── rol.py               # Modelo "Roles"
│   │   ├── usuario.py           # Modelo "Usuarios"
│   │   ├── pelicula.py          # Modelo "Peliculas"
│   │   ├── compra.py            # Modelo "Compras"
│   │   ├── pelicula_genero.py   # Modelo "Peliculas_Generos" (relación)
│   │
│   ├── services/                # Lógica de negocio independiente de las rutas
│   │   ├── __init__.py          # Inicialización de servicios
│   │   ├── generos_service.py   # Servicios para "Generos"
│   │   ├── roles_service.py     # Servicios para "Roles"
│   │   ├── usuarios_service.py  # Servicios para "Usuarios"
│   │   ├── peliculas_service.py # Servicios para "Peliculas"
│   │   ├── compras_service.py   # Servicios para "Compras"
│   │
│   ├── templates/               # Plantillas HTML (en caso de usarlas)
│   │   ├── base.html            # Layout base
│   │   ├── generos/             # Vistas de "Generos"
│   │   ├── roles/               # Vistas de "Roles"
│   │   ├── usuarios/            # Vistas de "Usuarios"
│   │   ├── peliculas/           # Vistas de "Peliculas"
│   │   ├── compras/             # Vistas de "Compras"
│   │
│   ├── static/                  # Archivos estáticos (CSS, JS, imágenes)
│       ├── css/                 # Hojas de estilo
│       ├── js/                  # Scripts
│       ├── images/              # Imágenes
│
├── migrations/                  # Migraciones de la base de datos (Flask-Migrate)
│
├── tests/                       # Tests unitarios y de integración
│   ├── test_generos.py          # Tests para "Generos"
│   ├── test_roles.py            # Tests para "Roles"
│   ├── test_usuarios.py         # Tests para "Usuarios"
│   ├── test_peliculas.py        # Tests para "Peliculas"
│   ├── test_compras.py          # Tests para "Compras"
│
├── .gitignore                   # Archivos a ignorar en Git
├── README.md                    # Documentación del proyecto
├── requirements.txt             # Dependencias del proyecto
├── run.py                       # Punto de entrada de la aplicación

Descripción de las carpetas principales:

app/:
Contiene toda la lógica del proyecto: rutas, modelos, y lógica de negocio.
Modulares por tabla para mantener un CRUD limpio y manejable.

routes/:
Define las rutas que manejan las operaciones CRUD.
Por ejemplo, generos_routes.py tendrá las rutas para crear, leer, actualizar y eliminar géneros.

models/:
Aquí se definen los modelos que reflejan la estructura de tu base de datos (tablas).
Puedes usar SQLAlchemy para mapear tus tablas a objetos.

services/:
Se coloca la lógica de negocio para que las rutas queden ligeras.
Ejemplo: validaciones, cálculos o reglas que no pertenecen al controlador.

templates/ y static/:
Para HTML, CSS, JS e imágenes si decides tener una interfaz web integrada.

migrations/:
Guarda los scripts de migración generados por Flask-Migrate.

tests/:
Contiene pruebas unitarias y de integración para validar las funcionalidades del sistema.