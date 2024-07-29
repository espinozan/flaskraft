# flaskraft
Flaskraft es una herramienta que simplifica el proceso de creación de un proyecto Flask, permitiendo a los desarrolladores enfocarse en el desarrollo de la aplicación en lugar de la configuración inicial. 

Flaskraft
Flaskraft es una herramienta de automatización para la creación de proyectos Flask. Permite a los desarrolladores generar rápidamente una estructura de proyecto Flask personalizada, seleccionando características y configuraciones según sus necesidades. Flaskraft facilita la configuración inicial de un proyecto, ahorrando tiempo y asegurando que se sigan buenas prácticas desde el principio.

¿Qué es Flask?
Flask es un microframework de Python para el desarrollo de aplicaciones web. Es conocido por su simplicidad y flexibilidad, permitiendo a los desarrolladores crear aplicaciones web de manera rápida y eficiente. Flask proporciona las herramientas básicas para construir una aplicación web, y se puede extender con diversas extensiones para añadir funcionalidades adicionales.

¿Qué es Flaskraft y para qué sirve?
Flaskraft es una herramienta que simplifica el proceso de creación de un proyecto Flask, permitiendo a los desarrolladores enfocarse en el desarrollo de la aplicación en lugar de la configuración inicial. Con Flaskraft, puedes:

Generar automáticamente la estructura de un proyecto Flask.
Seleccionar la versión de Flask que deseas utilizar.
Elegir entre diferentes estructuras de proyecto según el tipo de aplicación que deseas desarrollar.
Configurar bases de datos, ORM, linters, pruebas, Docker, documentación y CI/CD.
Características
Creación de Proyectos: Crea automáticamente una estructura de proyecto Flask con archivos y directorios necesarios.
Selección de Versión de Flask: Instala la versión de Flask especificada por el usuario.
Estructuras de Proyecto: Elige entre diversas estructuras de proyecto predefinidas como minimal, API, monolithic, microservices, etc.
Configuración de Base de Datos: Soporte para múltiples bases de datos como PostgreSQL, MongoDB, MySQL, Oracle, SQL Server, SQLite, SurrealDB y MariaDB.
ORM y Linters: Opción para añadir SQLAlchemy como ORM y linters como flake8 y black.
Configuración de Pruebas: Añade pytest para la realización de pruebas unitarias.
Integración con Docker: Genera archivos Dockerfile y docker-compose.yml para la contenedorización del proyecto.
Documentación: Genera archivos de documentación como README.md y .env.
CI/CD: Configura integraciones continuas con GitHub Actions.
Beneficios
Ahorro de Tiempo: Automatiza la configuración inicial de un proyecto Flask.
Buenas Prácticas: Garantiza una estructura de proyecto organizada y siguiendo buenas prácticas.
Flexibilidad: Permite personalizar la configuración del proyecto según las necesidades del desarrollador.
Escalabilidad: Facilita la configuración de proyectos que pueden escalarse con el tiempo.
Facilidad de Uso: Interfaz de línea de comandos sencilla e intuitiva.

Requisitos
Python 3.6 o superior

Instalación
Clona este repositorio:

git clone https://github.com/espinozan/flaskraft.git
cd flaskraft
Asegúrate de tener Python 3.6 o superior instalado.

Uso
Ejecuta el script:

python flaskraft.py

Sigue las instrucciones en la terminal para ingresar el nombre del proyecto, la estructura deseada, la versión de Flask, la base de datos y otras configuraciones adicionales.

Opciones de Configuración
Estructuras de Proyecto Disponibles
Minimal: Estructura básica con la configuración mínima necesaria.
API: Configuración para una API RESTful.
Monolithic: Proyecto monolítico con templates y rutas integradas.
Microservices: Configuración para una arquitectura de microservicios.
Blogging: Proyecto para una plataforma de blogs.
E-commerce: Proyecto para una tienda en línea.
Dashboard: Configuración para una aplicación de tablero de control.
IoT: Proyecto para aplicaciones de Internet de las Cosas.
Data Analysis: Configuración para análisis de datos.
Single-page Application: Configuración para una aplicación de una sola página.
Multi-page Application: Configuración para una aplicación de múltiples páginas.
Bases de Datos Soportadas
PostgreSQL
MongoDB
MySQL
Oracle
SQL Server
SQLite
SurrealDB
MariaDB
Características Adicionales
Entorno Virtual: Creación de un entorno virtual para la gestión de dependencias.
ORM: Integración con SQLAlchemy.
Linters: Instalación de flake8 y black para análisis estático de código.
Pruebas: Configuración de pytest para pruebas unitarias.
Docker: Archivos de configuración para Docker y docker-compose.
Documentación: Generación de README.md y .env.
CI/CD: Configuración de CI/CD con GitHub Actions.
Archivos Generados
Dependiendo de las opciones seleccionadas, el script generará los siguientes archivos y directorios:

app.py: Archivo principal de la aplicación Flask.
requirements.txt: Dependencias del proyecto.
templates/: Directorio para plantillas HTML (si aplica).
Dockerfile y docker-compose.yml: Archivos de configuración de Docker (si aplica).
README.md: Archivo de documentación.
.env: Archivo de configuración de entorno.
.github/workflows/ci.yml: Archivo de configuración de CI/CD con GitHub Actions (si aplica).

Ejemplo de Estructura de Proyecto

nombre_del_proyecto/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── Dockerfile (si se selecciona)
├── docker-compose.yml (si se selecciona)
├── README.md
├── .env (si se selecciona)
└── .github/
    └── workflows/
        └── ci.yml (si se selecciona)
Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría realizar.

Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.
