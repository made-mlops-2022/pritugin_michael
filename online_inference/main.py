from fastapi import FastAPI, status, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pathlib import Path
from utils.model_utils import model_exists, download_model, StartupException
from utils.data import HeartRequest
from dotenv import load_dotenv, find_dotenv
import os
from sklearn.pipeline import Pipeline
import joblib
from loguru import logger
import warnings
import pandas as pd

warnings.filterwarnings("ignore")


app = FastAPI()

model: Pipeline = None


@app.on_event("startup")
def start_service():
    logger.info("Service is starting")
    load_dotenv(find_dotenv())

    model_path = os.getenv("MODEL_PATH")
    if model_path is None:
        logger.error("ENV variable MODEL_PATH does not exist")
        raise StartupException("ENV variable MODEL_PATH does not exist")

    model_path = Path(model_path)

    if not model_exists(model_path):
        logger.info("Model does not exist - starting to download the model")
        download_model(model_path)
        logger.info("Model is downloaded")

    global model
    model = joblib.load(model_path)
    logger.info("Model is loaded")

    logger.info("Preparations for the launch are over")


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
    return JSONResponse({"error": str(exc)}, status_code=400)


@app.post("/predict")
def predict(request: HeartRequest):
    request = pd.DataFrame([request.dict()])

    result = model.predict(request)

    return {"condition": int(result[0])}


@app.get("/health", status_code=status.HTTP_200_OK)
def health():
    global model
    if model is None:
        raise HTTPException(status_code=404, detail="Model not found")

    return {"status": "ok"}
