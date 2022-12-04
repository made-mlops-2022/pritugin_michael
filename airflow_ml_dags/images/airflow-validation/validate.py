import os
import pickle
import numpy as np
import mlflow

import click
import pandas as pd

VAL_DATA_PATH = "val_data.csv"
VAL_TARGET_PATH = "val_target.csv"

@click.command()
@click.option("--model_dir")
@click.option("--data_dir")
def validate(model_dir, data_dir):

    mlflow.set_tracking_uri("http://localhost:5000")
    model_name = os.listdir(model_dir)[0]
    task = model_name.split(".")[0][8:]

    with mlflow.start_run(run_id=task):    
        inputs = pd.read_csv(os.path.join(data_dir, VAL_DATA_PATH))
        target = pd.read_csv(os.path.join(data_dir, VAL_TARGET_PATH))

        with open(os.path.join(model_dir, model_name), 'rb') as fin:
            model = pickle.load(fin)

        target = target["target"]
        predictions = model.predict(inputs)
    
        err = np.mean(abs(predictions - target))

        with open(os.path.join(model_dir,  'metrics.txt'), "w") as out_file:
            out_file.write("MAE: {}".format(err))


if __name__ == '__main__':
    validate()
