import unittest
from heart.features.transformers import OneHotTransformer, DropTransformer
import pandas as pd
import numpy as np


class TestOneHotTransformer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        feature1 = [1, 2, 3, 4, 3, 4, 1, 2]
        feature2 = [0, 1, 1, 0, 0, 0, 1, 1]

        data = {"feature1": feature1, "feature2": feature2}

        cls.df = pd.DataFrame(data)
        cls.categorial_features = ["feature1"]
        cls.transform = OneHotTransformer(cls.categorial_features)

        right_dict = {
            "feature1_1": np.array(cls.df["feature1"] == 1, dtype=np.int32),
            "feature1_2": np.array(cls.df["feature1"] == 2, dtype=np.int32),
            "feature1_3": np.array(cls.df["feature1"] == 3, dtype=np.int32),
            "feature1_4": np.array(cls.df["feature1"] == 4, dtype=np.int32),
            "feature2": cls.df["feature2"],
        }
        cls.right_result = pd.DataFrame(right_dict)

    def test_fit_and_transform(self):
        df_test = self.df.copy(deep=True)
        self.transform.fit(df_test)
        # датафрейм не изменился
        self.assertTrue(pd.DataFrame.equals(self.df, df_test))

        result = self.transform.transform(df_test)

        # датафрейм не изменился
        self.assertTrue(pd.DataFrame.equals(self.df, df_test))

        self.assertEqual(result.shape[0], 8)
        self.assertEqual(result.shape[1], 5)

        self.assertTrue(pd.DataFrame.equals(result, self.right_result))

    def test_fit_transform(self):
        df_test = self.df.copy(deep=True)
        result = self.transform.fit_transform(df_test)

        # датафрейм не изменился
        self.assertTrue(pd.DataFrame.equals(self.df, df_test))

        self.assertEqual(result.shape[0], 8)
        self.assertEqual(result.shape[1], 5)

        self.assertTrue(pd.DataFrame.equals(result, self.right_result))


class TestDropTransformer(unittest.TestCase):
    def setUp(self):
        feature1 = [1, 2, 3, 4, 3, 4, 1, 2]
        feature2 = [0, 1, 1, 0, 0, 0, 1, 1]

        data = {"feature1": feature1, "feature2": feature2}

        self.df = pd.DataFrame(data)
        self.drop_features = ["feature1"]
        self.transform = DropTransformer(self.drop_features)

        right_dict = {
            "feature2": self.df["feature2"],
        }
        self.right_result = pd.DataFrame(right_dict)

    def test_fit_and_transform(self):
        df_test = self.df.copy(deep=True)
        self.transform.fit(df_test)
        # датафрейм не изменился
        self.assertTrue(pd.DataFrame.equals(self.df, df_test))

        result = self.transform.transform(df_test)

        # датафрейм не изменился
        self.assertTrue(pd.DataFrame.equals(self.df, df_test))

        self.assertEqual(result.shape[0], 8)
        self.assertEqual(result.shape[1], 1)

        self.assertTrue(pd.DataFrame.equals(result, self.right_result))

    def test_fit_transform(self):
        df_test = self.df.copy(deep=True)
        result = self.transform.fit_transform(df_test)

        # датафрейм не изменился
        self.assertTrue(pd.DataFrame.equals(self.df, df_test))

        self.assertEqual(result.shape[0], 8)
        self.assertEqual(result.shape[1], 1)

        self.assertTrue(pd.DataFrame.equals(result, self.right_result))
