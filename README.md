# Proyecto FastAPI + SQLAlchemy + Alembic

Este proyecto usa **FastAPI**, **SQLAlchemy** y **Alembic** para gestionar la base de datos PostgreSQL con migraciones.

---

## Requisitos

- Python 3.11.13 (recomendado, pero puede funcionar con Python ≥ 3.10)
- PostgreSQL versión 14.19 instalado y corriendo
- pip

> Nota: Alembic y otras dependencias se instalarán automáticamente desde `requirements.txt`.


## Clonar el proyecto

```bash
git clone https://github.com/tuusuario/tu_repositorio.git
cd tu_repositorio
```

## Creat entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows
```

## Instalar dependencias
```bash
pip install -r requirements.txt
```
Esto instalará:

- FastAPI
- SQLAlchemy
- Alembic
- psycopg2-binary (driver para PostgreSQL)
- python-dotenv



## Crear la base de datos
1. Asegúrate de que PostgreSQL esté corriendo.
2. Crea la base de datos (ejemplo usando psql o TablePlus):
```bash
# Para este caso usaremos psql en la terminal
psql -U postgres # Indica que vas a iniciar sesión con el usuario postgres(se crea por default)

\l # Te mostrará las BDs existentes, si no tienes ninguna solo se mostraran templates

# Crea la BD con el siguiente comando
CREATE DATABASE inbol_db;
```
3. Después de esto puedes cerrar la terminal.
4. Instala table plus


## Configurar variables de entorno
Crea un archivo .env en la raíz del proyecto con tu URL de conexión a PostgreSQL(Para esto deberás primero haber creado la BD de postgres en la terminal):
```bash
DATABASE_URL=postgresql://usuario:password@localhost:5432/mi_basedatos
```

## Aplicar migraciones con Alembic
Esto creará todas las tablas definidas en tus modelos:
```bash
alembic upgrade head
```

## Ejecutar app
```bash
uvicorn app.main:app --reload
```
- La API estará disponible en http://127.0.0.1:8000
- Documentación automática en http://127.0.0.1:8000/docs