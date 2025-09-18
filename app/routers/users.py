from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.users import User
from app.schemas import UserCreate, UserResponse
from app.utils.hash import hash_password

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Verifica si el usuario ya existe
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    # Crear un nuevo usuario
    new_user = User(
        name = user.name,
        apellido_paterno = user.apellido_paterno,
        apellido_materno = user.apellido_materno,
        email = user.email,
        password = hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id,  "email": new_user.email}
