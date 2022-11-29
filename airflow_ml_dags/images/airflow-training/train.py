import os
import pickle
import mlflow

import click
import pandas as pd
from sklearn.linear_model import LinearRegression

@click.command("train")
@click.option("--input_dir")
@click.option("--output_dir")

def train(input_dir, output_dir):
    mlflow.set_tracking_uri("http://localhost:5000")
    
    with mlflow.start_run(run_name="train"):
        run = mlflow.active_run()
        
        data = pd.read_csv(os.path.join(input_dir, "train_data.csv"))
        targets = pd.read_csv(os.path.join(input_dir, "train_target.csv"))
        clf = LinearRegression()
        clf.fit(data, targets["target"])
        
        model_params = clf.get_params()
        for param in model_params:
            mlflow.log_param(param, model_params[param])
            
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, f'lin_reg_{run.info.run_id}.pkl'), 'wb') as f:
            pickle.dump(clf, f)

        mlflow.sklearn.log_model(sk_model=clf, artifact_path="linear_model", registered_model_name='lin_reg')
        


if __name__ == '__main__':
    train()
