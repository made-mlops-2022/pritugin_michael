import os
import hydra
import pandas as pd
import numpy as np
from heart.conf.config import Config
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from heart.features.transformers import OneHotTransformer, DropTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_validate
from heart.models import LOCAL_MLFLOW_PATH
import joblib
from loguru import logger
import mlflow
from dotenv import load_dotenv, find_dotenv


@hydra.main(version_base=None, config_path="../conf", config_name="config")
def main(cfg: Config) -> None:
    if cfg.use_mlflow:
        load_dotenv(find_dotenv())
        mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
    else:
        mlflow.set_tracking_uri(f"file://{LOCAL_MLFLOW_PATH}")

    with mlflow.start_run():
        mlflow.log_param("model_type", cfg.model.model_type)
        if cfg.model.model_type == "logreg":
            C = cfg.model.C
            mlflow.log_param("C", cfg.model.C)
            clf = LogisticRegression(C=C, max_iter=10000)
            logger.info("Using Logistic Regression as model")
        elif cfg.model.model_type == "rf":
            max_depth = cfg.model.max_depth
            mlflow.log_param("max_depth", cfg.model.max_depth)
            clf = RandomForestClassifier(max_depth=max_depth)
            logger.info("Using Random Forest as model")

        mlflow.log_param("preprocessing_type", cfg.preprocessing.preprocessing_type)
        features = cfg.preprocessing.features
        if cfg.preprocessing.preprocessing_type == "onehot":
            transformer = OneHotTransformer
            logger.info("Using OneHotTransformer as preprocessing")
        elif cfg.preprocessing.preprocessing_type == "drop":
            transformer = DropTransformer
            logger.info("Using DropTransformer as preprocessing")

        logger.info("Read data")
        df = pd.read_csv(cfg.dataset_path)

        X = df.drop("condition", axis=1)
        y = df["condition"]
        X_train = transformer(features).fit_transform(X)

        metrics = ["precision_macro", "f1_macro", "recall_macro"]
        scores = cross_validate(clf, X_train, y, cv=5, scoring=metrics)

        for metric in metrics:
            mlflow.log_metric(metric, np.mean(scores[f"test_{metric}"]))

        pipe = Pipeline([("transformer", transformer(features)), ("model", clf)])
        logger.info("Starting model training")
        pipe.fit(X, y)
        logger.info("Model was trained")

        mt = cfg.model.model_type
        pt = cfg.preprocessing.preprocessing_type
        save_path = cfg.models_path / f"{mt}_{pt}.joblib"
        joblib.dump(
            pipe,
            save_path,
        )
        logger.info(f"The model was saved in {save_path}")

        if cfg.use_mlflow:
            mlflow.sklearn.log_model(pipe, "model", registered_model_name=f"{mt}_{pt}")
