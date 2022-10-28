import pandas as pd
from sklearn import preprocessing


if __name__ == "__main__":
    df = pd.read_csv("../../data/raw/heart_cleveland_upload.csv")

    df_cat = df[["cp", "restecg", "slope", "thal"]]
    df_other = df.drop(["cp", "restecg", "slope", "thal"], axis=1)

    encoder = preprocessing.OneHotEncoder()
    cat_array = encoder.fit_transform(df_cat).toarray()
    df_cat = pd.DataFrame(data=cat_array, columns=encoder.get_feature_names_out())

    df = pd.concat([df_cat, df_other], axis=1)

    df.to_csv("../../data/prepared/heart.csv", index=False)
