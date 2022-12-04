import pytest
from airflow.models import DagBag
import sys

sys.path.append("dags")

@pytest.fixture()
def dags():
    return DagBag(dag_folder="dags/", include_examples=False)

def test_generate_data(dags):
    assert "data_generator" in dags.dags
    assert len(dags.dags["data_generator"].tasks) == 1
    
    structure = {
        "docker-generation": []
    }
    dags_ = dags.dags["data_generator"]
    for dag, task in dags_.task_dict.items():
        assert set(structure[dag]) == task.downstream_task_ids


def test_train(dags):
    assert "train" in dags.dags
    assert len(dags.dags["train"].tasks) == 5
    
    content = {
        "airflow-wait-file": ["docker-airflow-preparing"],
        "docker-airflow-preparing": ["docker-airflow-splitting"],
        "docker-airflow-splitting": ['docker-airflow-training'],
        "docker-airflow-training": ["docker-airflow-validation"],
        "docker-airflow-validation": []
    }
    dag = dags.dags["train"]
    for name, task in dag.task_dict.items():
        assert set(content[name]) == task.downstream_task_ids


def test_predict(dags):
    assert "predict" in dags.dags
    assert len(dags.dags["predict"].tasks) == 1
    content = {
        "docker-airflow-prediction": []
    }
    dag = dags.dags["predict"]
    for name, task in dag.task_dict.items():
        assert set(content[name]) == task.downstream_task_ids
        
