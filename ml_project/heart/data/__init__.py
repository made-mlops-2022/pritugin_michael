import os
from pathlib import Path

RAW_PATH = (
    Path(os.environ["HEART_PROJECT"]) / "data" / "raw" / "heart_cleveland_upload.csv"
)
EDA_PATH = Path(os.environ["HEART_PROJECT"]) / "reports" / "EDA_report.html"
