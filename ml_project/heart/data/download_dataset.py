import boto3
from heart.data import RAW_PATH


def main():
    session = boto3.session.Session()
    s3_client = session.client(service_name="s3", endpoint_url="https://hb.bizmrg.com")

    s3_client.download_file(
        "mlflow_homework1", "heart/heart_cleveland_upload.csv", str(RAW_PATH)
    )


if __name__ == "__main__":
    main()
