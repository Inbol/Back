from pydantic import BaseModel, EmailStr, Field

# Schema para crear un usuario
class UserCreate(BaseModel):
    name: str = Field(..., max_length=50)
    apellido_paterno: str = Field(..., max_length=50)
    apellido_materno: str = Field(..., max_length=50)
    email: EmailStr
    password: str = Field(..., max_length=30)

# Schema para devolver información de usuario
class UserResponse(BaseModel):
    id: int
    name: str
    apellido_paterno: str
    apellido_materno: str
    email: EmailStr

    class Config:
        orm_mode = True

# Schema para crear una empresa
class EnterpriseCreate(BaseModel):
    enterprise_name: str = Field(..., max_length=60)
    email: EmailStr
    password: str = Field(..., max_length=30)

# Schema para devolver información una empresa
class EnterpriseResponse(BaseModel):
    id: int
    enterprise_name: str
    email: EmailStr

    class Config:
        orm_mode = True

# Schema que pide los datos del login
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# Schema qiue pide losn datos del predict
class PredictRequest(BaseModel):
    data: dict

