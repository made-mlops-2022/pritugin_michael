from hydra.core.config_store import ConfigStore
from dataclasses import dataclass
from omegaconf import MISSING


@dataclass
class ModelType:
    model_type: str


@dataclass
class PreprocessingType:
    preprocessing_type: str


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
    preprocessing_type: str = "one_hot_encoding"


@dataclass
class Config:
    model: ModelType
    preprocessing: PreprocessingType


cs = ConfigStore.instance()
cs.store(name="base_config", node=Config)
cs.store(group="model", name="base_logreg", node=LogReg)
cs.store(group="model", name="base_rf", node=RF)
cs.store(group="preprocessing", name="base_onehot", node=OneHotEncoding)
