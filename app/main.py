from fastapi import FastAPI
from app.routers import user_router

app = FastAPI()

# Registrar routers
app.include_router(user_router.router)