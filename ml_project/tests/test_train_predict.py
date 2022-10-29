import unittest
from heart.models.train import main as train
from heart.models.predict import main as predict
from heart.conf.config import Config, LogReg, OneHotEncoding, RF, DropFeatures
from .utils import generate_data
from tempfile import NamedTemporaryFile, TemporaryDirectory
from pathlib import Path
from click.testing import CliRunner


class TestTrain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.models_dir = TemporaryDirectory()
        cls.MODELS_PATH = Path(cls.models_dir.name)

        cls.train_file = NamedTemporaryFile()
        cls.TRAIN_PATH = Path(cls.train_file.name)

        cls.test_file = NamedTemporaryFile()
        cls.TEST_PATH = Path(cls.test_file.name)

        cls.output_file = NamedTemporaryFile()
        cls.OUTPUT_PATH = Path(cls.output_file.name)

        train_dataset_size = 300
        dataset = generate_data(train_dataset_size)
        dataset.to_csv(cls.TRAIN_PATH, index=False)

        cls.test_dataset_size = 300
        dataset = generate_data(cls.test_dataset_size, is_test=True)
        dataset.to_csv(cls.TEST_PATH, index=False)

        cls.features = ["cp", "restecg", "slope", "thal"]
        cls.runner = CliRunner()

    def test_train_1(self):
        config = Config(
            LogReg(C=1.0),
            OneHotEncoding(features=self.features),
            self.TRAIN_PATH,
            self.MODELS_PATH,
        )

        train(config)

        model_path = self.MODELS_PATH / "logreg_onehot.joblib"
        self.assertTrue(model_path.is_file())

        result = self.runner.invoke(
            predict,
            [
                "--model",
                str(model_path),
                "--dataset",
                str(self.TEST_PATH),
                "--output",
                str(self.OUTPUT_PATH),
            ],
        )

        self.assertEqual(result.exit_code, 0)

        self.assertTrue(self.OUTPUT_PATH.is_file())

        with self.OUTPUT_PATH.open("r") as fin:
            targets = [int(line) for line in fin]

        self.assertEqual(len(targets), self.test_dataset_size)
        self.assertEqual(set(targets), {0, 1})

    def test_train_2(self):
        config = Config(
            LogReg(C=1.0),
            DropFeatures(features=self.features),
            self.TRAIN_PATH,
            self.MODELS_PATH,
        )

        train(config)

        model_path = self.MODELS_PATH / "logreg_drop.joblib"
        self.assertTrue(model_path.is_file())

        result = self.runner.invoke(
            predict,
            [
                "--model",
                str(model_path),
                "--dataset",
                str(self.TEST_PATH),
                "--output",
                str(self.OUTPUT_PATH),
            ],
        )

        self.assertEqual(result.exit_code, 0)

        self.assertTrue(self.OUTPUT_PATH.is_file())

        with self.OUTPUT_PATH.open("r") as fin:
            targets = [int(line) for line in fin]

        self.assertEqual(len(targets), self.test_dataset_size)
        self.assertEqual(set(targets), {0, 1})

    def test_train_3(self):
        config = Config(
            RF(max_depth=5),
            OneHotEncoding(features=self.features),
            self.TRAIN_PATH,
            self.MODELS_PATH,
        )

        train(config)

        model_path = self.MODELS_PATH / "rf_onehot.joblib"
        self.assertTrue(model_path.is_file())

        result = self.runner.invoke(
            predict,
            [
                "--model",
                str(model_path),
                "--dataset",
                str(self.TEST_PATH),
                "--output",
                str(self.OUTPUT_PATH),
            ],
        )

        self.assertEqual(result.exit_code, 0)

        self.assertTrue(self.OUTPUT_PATH.is_file())

        with self.OUTPUT_PATH.open("r") as fin:
            targets = [int(line) for line in fin]

        self.assertEqual(len(targets), self.test_dataset_size)
        self.assertEqual(set(targets), {0, 1})

    def test_train_4(self):
        config = Config(
            RF(max_depth=5),
            DropFeatures(features=self.features),
            self.TRAIN_PATH,
            self.MODELS_PATH,
        )

        train(config)

        model_path = self.MODELS_PATH / "rf_drop.joblib"
        self.assertTrue(model_path.is_file())

        result = self.runner.invoke(
            predict,
            [
                "--model",
                str(model_path),
                "--dataset",
                str(self.TEST_PATH),
                "--output",
                str(self.OUTPUT_PATH),
            ],
        )

        self.assertEqual(result.exit_code, 0)

        self.assertTrue(self.OUTPUT_PATH.is_file())

        with self.OUTPUT_PATH.open("r") as fin:
            targets = [int(line) for line in fin]

        self.assertEqual(len(targets), self.test_dataset_size)
        self.assertEqual(set(targets), {0, 1})

    @classmethod
    def tearDownClass(cls):
        cls.models_dir.cleanup()
        cls.train_file.close()
        cls.test_file.close()
        cls.output_file.close()
