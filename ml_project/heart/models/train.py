import hydra
import pandas as pd
from heart.conf.config import Config
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from heart.data import PROCESSED_PATH
from heart.models import MODELS_PATH
import joblib


@hydra.main(version_base=None, config_path="../conf", config_name="config")
def main(cfg: Config) -> None:
    if cfg.model.model_type == "logreg":
        C = cfg.model.C
        clf = LogisticRegression(C=C, max_iter=10000)
    elif cfg.model.model_type == "rf":
        max_depth = cfg.model.max_depth
        clf = RandomForestClassifier(max_depth=max_depth)

    df = pd.read_csv(PROCESSED_PATH)

    X = df.drop("condition", axis=1)
    y = df["condition"]

    clf.fit(X, y)

    joblib.dump(clf, MODELS_PATH / f"{cfg.model.model_type}.joblib")


if __name__ == "__main__":
    main()
