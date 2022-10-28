import os
from pathlib import Path

RAW_PATH = (
    Path(os.environ["HEART_PROJECT"]) / "data" / "raw" / "heart_cleveland_upload.csv"
)
PROCESSED_PATH = (
    Path(os.environ["HEART_PROJECT"])
    / "data"
    / "processed"
    / "heart_cleveland_upload.csv"
)
