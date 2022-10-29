from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import preprocessing
import pandas as pd
import numpy as np


class OneHotTransformer(TransformerMixin, BaseEstimator):
    def __init__(self, categorial_features: list[str]):
        super().__init__()

        self.encoder = preprocessing.OneHotEncoder()
        self.categorial_features = categorial_features

    def fit(self, X: pd.DataFrame, y=None):
        categorial_data = X[self.categorial_features]

        self.encoder.fit(categorial_data)

        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        categorial_data = X[self.categorial_features]
        other_data = X.drop(self.categorial_features, axis=1)

        categorial_array = self.encoder.transform(categorial_data).toarray()
        categorial_array = categorial_array.astype(np.int32, copy=False)

        column_names = self.encoder.get_feature_names_out()
        new_categorial_data = pd.DataFrame(data=categorial_array, columns=column_names)

        transformed_df = pd.concat([new_categorial_data, other_data], axis=1)

        return transformed_df


class DropTransformer(TransformerMixin, BaseEstimator):
    def __init__(self, drop_features: list[str]):
        super().__init__()

        self.drop_features = drop_features

    def fit(self, X: pd.DataFrame, y=None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        transformed_df = X.drop(self.drop_features, axis=1)

        return transformed_df
