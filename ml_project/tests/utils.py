from faker import Faker
import pandas as pd


def generate_data(rows_count, is_test=False):
    fake = Faker()
    rows = [
        {
            "sex": fake.random_int(min=0, max=1),
            "cp": fake.random_int(min=0, max=4),
            "fbs": fake.random_int(min=0, max=1),
            "restecg": fake.random_int(min=0, max=2),
            "exang": fake.random_int(min=0, max=1),
            "slope": fake.random_int(min=0, max=2),
            "ca": fake.random_int(min=0, max=4),
            "thal": fake.random_int(min=0, max=2),
            "age": fake.random_int(min=29, max=77),
            "trestbps": fake.random_int(min=94, max=200),
            "chol": fake.random_int(min=126, max=564),
            "thalach": fake.random_int(min=71, max=202),
            "oldpeak": fake.pyfloat(min_value=0, max_value=6.2),
            "condition": fake.random_int(min=0, max=1),
        }
        for x in range(rows_count)
    ]

    df = pd.DataFrame(rows)
    if is_test:
        df.drop("condition", axis=1, inplace=True)

    return df
