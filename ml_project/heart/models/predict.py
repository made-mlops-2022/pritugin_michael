import click
import joblib
import pandas as pd
from loguru import logger


@click.command()
@click.option(
    "--model",
    help="Pretrained model path.",
    type=click.Path(exists=True),
    required=True,
)
@click.option(
    "--dataset",
    help="Input dataset in csv format.",
    type=click.Path(exists=True),
    required=True,
)
@click.option(
    "--output",
    help="Output file with predicted labels.",
    type=click.Path(),
    required=True,
)
def main(model: str, dataset: str, output: str):
    logger.info("Load model")
    clf = joblib.load(model)

    logger.info("Load dataset")
    data = pd.read_csv(dataset)

    logger.info("Start of prediction")
    pred = clf.predict(data)

    with open(output, "w") as fout:
        for target in pred:
            print(target, file=fout)
    logger.info(f"Result of prediction was saved in {output}")
