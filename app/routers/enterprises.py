from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.enterprises import Enterprise
from app.schemas import EnterpriseCreate, EnterpriseResponse
from app.utils.hash import hash_password

router = APIRouter(prefix="/enterprises", tags=["Enterprise"])

@router.post("/")
def create_enterprise(enterprise: EnterpriseCreate, db: Session = Depends(get_db)):
    # Verifica si la empresa ya existe
    existing_user = db.query(Enterprise).filter(Enterprise.email == enterprise.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="La emoresa ya existe")

    # Crear una nueva empresa
    new_enterprise = Enterprise(
        enterprise_name = enterprise.enterprise_name,
        email = enterprise.email,
        password = hash_password(enterprise.password)
    )
    db.add(new_enterprise)
    db.commit()
    db.refresh(new_enterprise)
    return {"id": new_enterprise.id,  "email": new_enterprise.email}
