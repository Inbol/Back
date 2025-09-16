from sqlalchemy import (
    Integer, String, Column
)
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    apellido_paterno = Column(String(50), nullable=False)
    apellido_materno = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False, index=True)
    password = Column(String(30), nullable=False)
