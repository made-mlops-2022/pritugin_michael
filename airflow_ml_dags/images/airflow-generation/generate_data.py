import os

import click
import pandas as pd
import numpy as np

from sklearn.datasets import load_boston

INPUTS_PATH = "data.csv"
TARGETS_PATH = "target.csv"


@click.command("generate")
@click.option("--output_dir")
def download(output_dir):
    boston_dataset = load_boston()
    boston = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
    
    X = pd.DataFrame(np.c_[boston['LSTAT'], boston['RM'], boston['PTRATIO']], columns = ['LSTAT','RM', 'PTRATIO'])
    Y = boston_dataset.target
    
    os.makedirs(output_dir, exist_ok=True)
    Y = pd.DataFrame(Y, columns=["target"])
    
    X.to_csv(os.path.join(output_dir, INPUTS_PATH), index=False)
    Y.to_csv(os.path.join(output_dir, TARGETS_PATH), index=False)


if __name__ == '__main__':
    download()
