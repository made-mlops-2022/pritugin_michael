import os
from datetime import timedelta, date

from airflow.sensors.python import PythonSensor
import pendulum
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
from constants import *

    
with DAG(
        "train",
        default_args=default_args,
        schedule_interval="@weekly",
        start_date=pendulum.today('UTC').add(days=0),
) as dag:

    wait_data = PythonSensor(
        task_id="airflow-wait-file",
        python_callable=is_exists,
        timeout=6000,
        poke_interval=10,
        retries=100,
        mode="poke",
    )

    prepare_data = DockerOperator(
        image="airflow-preparing",
        command="--input_dir {} --output_dir {}".format(RAW_DATA, PROCESSED_DATA),
        task_id="docker-airflow-preparing",
        do_xcom_push=False,
        auto_remove=True,
        network_mode="bridge",
        mounts=[MOUNT_SOURCE]
    )
    
    
    split_data = DockerOperator(
        image="airflow-splitting",
        command="--input_dir {}".format(PROCESSED_DATA),
        task_id="docker-airflow-splitting",
        do_xcom_push=False,
        auto_remove=True,
        network_mode="bridge",
        mounts=[MOUNT_SOURCE]
    )
    
    train = DockerOperator(
        image="airflow-training",
        command="--input_dir {} --output_dir {}".format(PROCESSED_DATA, OUT_PATH),
        task_id="docker-airflow-training",
        do_xcom_push=True,
        auto_remove=True,
        network_mode="host",
        mounts=[MOUNT_SOURCE, Mount(source=LOCAL_MLRUNS_DIR, target='/mlruns', type='bind')]
    )

    validate = DockerOperator(
        image="airflow-validation",
        command="--model_dir {} --data_dir {}".format(OUT_PATH, PROCESSED_DATA),
        task_id="docker-airflow-validation",
        do_xcom_push=False,
        auto_remove=True,
        network_mode="host",
        mounts=[MOUNT_SOURCE, Mount(source=LOCAL_MLRUNS_DIR, target='/mlruns', type='bind')]
    )

    wait_data >> prepare_data >> split_data >> train >> validate
