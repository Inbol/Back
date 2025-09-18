from fastapi import FastAPI
from app.database import engine, Base
import app.models
from app.routers import users, enterprises# Importación de las rutas

app = FastAPI()

# Registrar routers
app.include_router(users.router)
app.include_router(enterprises.router)