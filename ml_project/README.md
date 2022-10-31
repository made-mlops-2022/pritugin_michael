Homework MADE-2022 MLOps
==============================
[![check](https://github.com/made-mlops-2022/pritugin_michael/actions/workflows/ci.yml/badge.svg?branch=homework1)](https://github.com/made-mlops-2022/pritugin_michael/actions/workflows/ci.yml)

## How to install
```bash
bash install.sh
```

### For use mlflow and dvc you need to configurate ~/.aws/credentials
Example:
```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```

### And you have to configurate .env file
Example:
```
MLFLOW_TRACKING_URI = YOUR_TRACKIN_URI
MLFLOW_S3_ENDPOINT_URL = YOUR_S3_ENDPOINT
```
by default project uses VK Cloud S3

-----------------------------

## How to download dataset

### Using command line utility
```bash
download_dataset
```

### Using DVC
```bash
dvc repro download_dataset
```

### Simple run python
```bash
python heart/data/download_dataset.py
```
-----------------------------

## How to train

### Using command line utility
```bash
train <hydra options>
```

### Using DVC
```bash
dvc repro train_model
```

### Simple run python
```bash
python heart/data/train.py <hydra options>
```

-----------------------------

## How to predict

### Using command line utility
```bash
predict [OPTIONS]
```

### Simple run python
```bash
python heart/data/predict.py [OPTIONS]
```

-----------------------------

## How to run tests
```bash
python -m unittest tests/test_*.py
```

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── heart              <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── conf           <- training configs
    │   │
    │   ├── data           <- code to download or generate data
    │   │
    │   ├── features       <- code to turn raw data into features for modeling
    │   │
    │   ├── models         <- code to train models and then use trained models
    │   │
    └── tests              <- tests for the project (train, predict, transformers)


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
