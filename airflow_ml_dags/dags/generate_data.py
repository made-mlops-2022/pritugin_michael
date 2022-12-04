from datetime import timedelta
import pendulum
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
from constants import *

with DAG(
        "data_generator",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=pendulum.today('UTC').add(days=0),
) as dag:
    generate = DockerOperator(
        image="airflow-generation",
        command=f"--output_dir {RAW_DATA}",
        task_id="docker-generation",
        do_xcom_push=False,
        network_mode="bridge",
        mounts=[Mount(source=MOUNT_PATH, target="/data", type='bind')]
    )

    generate
