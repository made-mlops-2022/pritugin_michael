import hydra
import pandas as pd
from heart.conf.config import Config
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from heart.features.transformers import OneHotTransformer, DropTransformer
from sklearn.pipeline import Pipeline
import joblib
from loguru import logger


@hydra.main(version_base=None, config_path="../conf", config_name="config")
def main(cfg: Config) -> None:
    if cfg.model.model_type == "logreg":
        C = cfg.model.C
        clf = LogisticRegression(C=C, max_iter=10000)
        logger.info("Using Logistic Regression as model")
    elif cfg.model.model_type == "rf":
        max_depth = cfg.model.max_depth
        clf = RandomForestClassifier(max_depth=max_depth)
        logger.info("Using Random Forest as model")

    features = cfg.preprocessing.features
    if cfg.preprocessing.preprocessing_type == "onehot":
        transformer = OneHotTransformer(features)
        logger.info("Using OneHotTransformer as preprocessing")
    elif cfg.preprocessing.preprocessing_type == "drop":
        transformer = DropTransformer(features)
        logger.info("Using DropTransformer as preprocessing")

    logger.info("Read data")
    df = pd.read_csv(cfg.dataset_path)

    X = df.drop("condition", axis=1)
    y = df["condition"]

    pipe = Pipeline([("transformer", transformer), ("model", clf)])

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
