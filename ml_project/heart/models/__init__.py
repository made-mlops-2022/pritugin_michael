import os
from pathlib import Path

MODELS_PATH = Path(os.environ["HEART_PROJECT"]) / "models"
LOCAL_MLFLOW_PATH = Path(os.environ["HEART_PROJECT"]) / "mlruns"
