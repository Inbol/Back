from app.schemas import LoginRequest
from app.utils.hash import verify_password
from app.models.users import User
from app.models.enterprises import Enterprise
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter

router = APIRouter(prefix="/login", tags=["Login"])

@router.post("/")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    # Primero buscamos en usuarios
    user = db.query(User).filter(User.email == request.email).first()
    if user:
        if not verify_password(request.password, user.password):
            raise HTTPException(status_code=400, detail="Contraseña incorrecta")
        return {"message": "Login exitoso", "type": "user", "id": user.id, "email": user.email}

    # Si no es usuario, buscamos en empresas
    enterprise = db.query(Enterprise).filter(Enterprise.email == request.email).first()
    if enterprise:
        if not verify_password(request.password, enterprise.password):
            raise HTTPException(status_code=400, detail="Contraseña incorrecta")
        return {"message": "Login exitoso", "type": "enterprise", "id": enterprise.id, "email": enterprise.email}

    # Si no existe en ninguna tabla
    raise HTTPException(status_code=400, detail="Email no registrado")
