from sqlalchemy import (
    Integer, String, Column
)
from app.database import Base

class Enterprise(Base):
    __tablename__ = "enterprise"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    enterprise_name = Column(String(60), nullable=False)
    email = Column(String(120), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
