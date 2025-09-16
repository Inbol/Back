from fastapi import FastAPI
from app.database import engine, Base
import app.models
from app.routers import users # Importación de la ruta de users

app = FastAPI()

# Crea todas las tablas si no existen
Base.metadata.create_all(bind=engine)

# Registrar routers
app.include_router(users.router)