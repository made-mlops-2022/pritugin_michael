import os
from datetime import timedelta, date

import pendulum
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.python import PythonSensor
from airflow.models import Variable
from docker.types import Mount
from constants import *

with DAG(
        "predict",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=pendulum.today('UTC').add(days=0),
) as dag:
        
    predict = DockerOperator(
        image="airflow-prediction",
        command="--input_dir {} --model_dir {} --out_dir {}".format(PROCESSED_DATA, MODEL, PREDICTIONS_PATH),
        task_id="docker-airflow-prediction",
        do_xcom_push=False,
        network_mode="host",
        mounts=[MOUNT_SOURCE, Mount(source=LOCAL_MLRUNS_DIR, target='/mlruns', type='bind')]
    )

    predict
