import pandas as pd
import sweetviz as sv
from heart.data import RAW_PATH, EDA_PATH

if __name__ == "__main__":
    df = pd.read_csv(RAW_PATH)
    report = sv.analyze([df, "Heart Disease"])
    report.show_html(EDA_PATH)
