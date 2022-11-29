import os
import click
import pandas as pd
from sklearn.preprocessing import StandardScaler

@click.command("prepare")
@click.option("--input_dir")
@click.option("--output_dir")

def prepare_data(input_dir, output_dir):

    data = pd.read_csv(os.path.join(input_dir, "data.csv"))
    target = pd.read_csv(os.path.join(input_dir, "target.csv"))
    
    scaler = StandardScaler()
    data_normalized = scaler.fit_transform(data)
    data_normalized = pd.DataFrame(data=data_normalized, columns=data.columns)
    
    os.makedirs(output_dir, exist_ok=True)
    
    data_normalized.to_csv(os.path.join(output_dir, "data_normalized.csv"), index=False)
    target.to_csv(os.path.join(output_dir, "target.csv"), index=False)


if __name__ == '__main__':
    prepare_data()
