import os
import subprocess

def create_project():
    project_name = input("Ingrese el nombre del proyecto: ").strip()
    if not project_name:
        print("El nombre del proyecto no puede estar vacío.")
        return

    flask_version = input("¿Desea la última versión de Flask? (1: Si, 2: No, ingrese la versión): ").strip()
    if flask_version == "" or flask_version == "1":
        flask_version = "flask"
    elif flask_version == "2":
        flask_version = input("Ingrese la versión de Flask (e.g., 2.0.1): ").strip()
        if not flask_version:
            print("La versión de Flask no puede estar vacía.")
            return
        flask_version = f"flask=={flask_version}"
    else:
        print("Opción no válida. Se instalará la última versión de Flask.")
        flask_version = "flask"

    structures = [
        "minimal", "api", "monolithic", "microservices", "blogging",
        "ecommerce", "dashboard", "iot", "data analysis",
        "single-page application", "multi-page application"
    ]
    print("Seleccione la estructura del proyecto:")
    for i, structure in enumerate(structures, 1):
        print(f"{i}. {structure}")
    structure_choice = input("Ingrese el número correspondiente: ").strip()
    try:
        structure_choice = int(structure_choice)
        if structure_choice < 1 or structure_choice > len(structures):
            raise ValueError
        project_structure = structures[structure_choice - 1]
    except ValueError:
        print("Selección no válida.")
        return

    venv_choice = input("¿Desea crear un entorno virtual? (S/N): ").strip().lower()
    create_venv = venv_choice == "s"

    databases = ["PostgreSQL", "MongoDB", "MySQL", "Oracle", "SQL Server", "SQLite", "SurrealDB", "MariaDB"]
    print("Seleccione la base de datos:")
    for i, db in enumerate(databases, 1):
        print(f"{i}. {db}")
    db_choice = input("Ingrese el número correspondiente: ").strip()
    try:
        db_choice = int(db_choice)
        if db_choice < 1 or db_choice > len(databases):
            raise ValueError
        db_type = databases[db_choice - 1]
    except ValueError:
        print("Selección no válida.")
        return

    use_orm = input("¿Desea utilizar un ORM? (S/N): ").strip().lower() == "s"
    install_linters = input("¿Desea instalar linters? (S/N): ").strip().lower() == "s"
    configure_testing = input("¿Desea configurar pruebas? (S/N): ").strip().lower() == "s"
    configure_docker = input("¿Desea configurar Docker? (S/N): ").strip().lower() == "s"
    generate_docs = input("¿Desea generar documentación? (S/N): ").strip().lower() == "s"
    setup_ci_cd = input("¿Desea configurar CI/CD? (S/N): ").strip().lower() == "s"

    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)

    if create_venv:
        subprocess.run(["python", "-m", "venv", "venv"])
        subprocess.run([os.path.join("venv", "Scripts", "activate.bat" if os.name == "nt" else "activate")])

    with open("requirements.txt", "w") as f:
        f.write(f"{flask_version}\n")
        if db_type:
            if db_type == "PostgreSQL":
                f.write("psycopg2-binary\n")
            elif db_type == "MongoDB":
                f.write("pymongo\n")
            elif db_type == "MySQL":
                f.write("mysqlclient\n")
            elif db_type == "Oracle":
                f.write("cx_Oracle\n")
            elif db_type == "SQL Server":
                f.write("pyodbc\n")
            elif db_type == "SQLite":
                f.write("pysqlite3\n")
            elif db_type == "SurrealDB":
                f.write("surrealdb\n")
            elif db_type == "MariaDB":
                f.write("mariadb\n")

        if use_orm:
            f.write("sqlalchemy\n")
        if install_linters:
            f.write("flake8\nblack\n")
        if configure_testing:
            f.write("pytest\n")

    templates = {
        "minimal": """from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
""",
        "api": """from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api")
def api():
    return jsonify({"message": "Hello, API!"})

if __name__ == "__main__":
    app.run(debug=True)
""",
        "monolithic": """from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
""",
        # Add other templates for different structures
    }

    os.makedirs("templates", exist_ok=True)
    with open(os.path.join("templates", "index.html"), "w") as f:
        f.write("<h1>Welcome to your Flask Project!</h1>")

    with open("app.py", "w") as f:
        f.write(templates.get(project_structure, templates["minimal"]))

    if configure_docker:
        with open("Dockerfile", "w") as f:
            f.write("FROM python:3.9\n")
            f.write("WORKDIR /app\n")
            f.write("COPY . .\n")
            f.write("RUN pip install -r requirements.txt\n")
            f.write('CMD ["flask", "run", "--host=0.0.0.0"]\n')

        with open("docker-compose.yml", "w") as f:
            f.write("version: '3.8'\n")
            f.write("services:\n")
            f.write("  app:\n")
            f.write("    build: .\n")
            f.write('    ports:\n')
            f.write('      - "5000:5000"\n')

    if generate_docs:
        with open("README.md", "w") as f:
            f.write(f"# {project_name}\n\n")
            f.write("Este es un proyecto Flask generado automáticamente.\n")

        with open(".env", "w") as f:
            f.write(f"FLASK_APP={project_name}\n")
            f.write("FLASK_ENV=development\n")

    if setup_ci_cd:
        os.makedirs(".github/workflows", exist_ok=True)
        with open(".github/workflows/ci.yml", "w") as f:
            f.write("name: CI\n")
            f.write("on: [push]\n")
            f.write("jobs:\n")
            f.write("  build:\n")
            f.write("    runs-on: ubuntu-latest\n")
            f.write("    steps:\n")
            f.write("      - uses: actions/checkout@v2\n")
            f.write("      - name: Set up Python\n")
            f.write("        uses: actions/setup-python@v2\n")
            f.write("        with:\n")
            f.write("          python-version: 3.9\n")
            f.write("      - name: Install dependencies\n")
            f.write("        run: |\n")
            f.write("          python -m pip install --upgrade pip\n")
            f.write("          pip install -r requirements.txt\n")
            f.write("      - name: Run tests\n")
            f.write("        run: pytest\n")

    print("Configuración completa. Su proyecto Flask está listo.")

if __name__ == "__main__":
    create_project()
