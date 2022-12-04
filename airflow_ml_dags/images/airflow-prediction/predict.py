import os
import pickle
import click
import pandas as pd
import mlflow.pyfunc

input_file = "data_normalized.csv"

@click.command("predict")
@click.option("--input_dir")
@click.option("--model_dir")
@click.option("--out_dir")
def predict(input_dir, model_dir, out_dir):

    data = pd.read_csv(os.path.join(input_dir, input_file))
    
    mlflow.set_tracking_uri("http://localhost:5000")

    model = mlflow.pyfunc.load_model(model_uri='models:/lin_reg/Production')   
 
    preds = model.predict(data)
    
    os.makedirs(out_dir, exist_ok=True)
    pred = pd.DataFrame(preds)
    pred.to_csv(os.path.join(out_dir, "predictions.csv"), index=False)


if __name__ == '__main__':
    predict()
