from pathlib import Path
import boto3
from botocore import UNSIGNED
from botocore.config import Config


def download_model(path: Path):
    session = boto3.session.Session()
    s3_client = session.client(
        service_name="s3",
        endpoint_url="https://hb.bizmrg.com",
        config=Config(signature_version=UNSIGNED),
    )

    s3_client.download_file("mlops_homework2", "model.joblib", str(path))


def model_exists(path: Path):
    return path.exists()


class StartupException(Exception):
    pass
