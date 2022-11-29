import os
from docker.types import Mount
from datetime import timedelta, date
from airflow.models import Variable
from airflow.utils.email import send_email_smtp

LOCAL_DATA_DIR = Variable.get('local_data_dir')
LOCAL_MLRUNS_DIR = Variable.get('local_mlruns_dir')


RAW_DATA = "/data/raw/{{ ds }}"
PROCESSED_DATA = "/data/processed/{{ ds }}"

OUT_PATH = "/data/models/lin_reg/{{ ds }}"

INFERENCE_DATA_PATH = "data_normalized.csv"
MODEL_NAME = "model.pkl"
PREDS_PATH = "predictions.csv"

PREDICTIONS_PATH = "/data/predictions/{{ ds }}"

MOUNT_PATH = "/home/viliar/ml-hdd/mlops/hw3_final/airflow_ml_dags/data/"

MODEL_PATH = Variable.get("MODEL_PATH")
MODEL = MODEL_PATH

MOUNT_SOURCE = Mount(source=MOUNT_PATH, target="/data", type='bind')

def failure_function(context):
    dag_run = context.get('dag_run')
    task_instances = dag_run.get_task_instances()
    text = "These task instances failed: {}".format(task_instances)
    send_email_smtp(to=default_args['email'], subject=text)
    
default_args = {
    "owner": "airflow",
    "email": ["viliar@mail.ru"],
    "email_on_failure": True,
    "on_failure_callback": failure_function,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

def is_exists():
    path = os.path.join("/opt/airflow/data/raw", date.today().strftime("%Y-%m-%d"))
    d = os.path.exists(os.path.join(path, "data.csv"))
    t = os.path.exists(os.path.join(path, "target.csv"))
    return d and t
