import os

import click
import pandas as pd
from sklearn.model_selection import train_test_split

@click.command("split")
@click.option("--input_dir")
def split_data(input_dir):
    X = pd.read_csv(os.path.join(input_dir, "data_normalized.csv"))
    y = pd.read_csv(os.path.join(input_dir, "target.csv"))
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=123)
    
    X_train.to_csv(os.path.join(input_dir, "train_data.csv"), index=False)
    y_train.to_csv(os.path.join(input_dir, "train_target.csv"), index=False)
    X_val.to_csv(os.path.join(input_dir, "val_data.csv"), index=False)
    y_val.to_csv(os.path.join(input_dir, "val_target.csv"), index=False)


if __name__ == '__main__':
    split_data()
