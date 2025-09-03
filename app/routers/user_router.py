from fastapi import APIRouter
from app.controllers import user_controller

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users():
    return user_controller.get_all_users()
