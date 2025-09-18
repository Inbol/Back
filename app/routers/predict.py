from app.schemas import PredictRequest
from fastapi import Depends, HTTPException, APIRouter
import numpy as np
import pandas as pd
import joblib
import os

router = APIRouter(prefix="/predict", tags=["Predict"])

# Carpeta donde está este script
BASE_DIR = os.path.dirname(__file__)
modelo_path = os.path.join(BASE_DIR, "modelo.pkl")

modelo = joblib.load(modelo_path)

@router.post("/")
def predict(request: PredictRequest):
    data = pd.DataFrame([request.data])

    prediccion = modelo.predict(data)

    # Predecir resultado
    return {"message": prediccion.tolist()}
