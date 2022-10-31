from hydra.core.config_store import ConfigStore
from dataclasses import dataclass
from omegaconf import MISSING
from pathlib import Path
from heart.data import RAW_PATH
from heart.models import MODELS_PATH


@dataclass
class ModelType:
    model_type: str


@dataclass
class PreprocessingType:
    preprocessing_type: str = MISSING
    features: list[str] = MISSING


@dataclass
class LogReg(ModelType):
    model_type: str = "logreg"
    C: float = MISSING


@dataclass
class RF(ModelType):
    model_type: str = "rf"
    max_depth: int = MISSING


@dataclass
class OneHotEncoding(PreprocessingType):
    preprocessing_type: str = "onehot"


@dataclass
class DropFeatures(PreprocessingType):
    preprocessing_type: str = "drop"


@dataclass
class Config:
    model: ModelType
    preprocessing: PreprocessingType
    dataset_path: Path = RAW_PATH
    models_path: Path = MODELS_PATH
    test_size: float = 0.2
    use_mlflow: bool = True


cs = ConfigStore.instance()
cs.store(name="base_config", node=Config)
cs.store(group="model", name="base_logreg", node=LogReg)
cs.store(group="model", name="base_rf", node=RF)
cs.store(group="preprocessing", name="base_onehot", node=OneHotEncoding)
cs.store(group="preprocessing", name="base_drop", node=DropFeatures)
