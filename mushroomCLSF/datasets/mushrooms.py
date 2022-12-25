import pandas as pd
from sklearn import preprocessing
from djangoBE.settings import BASE_DIR
import os

DATAFILE_PATH = os.path.join(BASE_DIR, 'mushroomCLSF/datasets/mushrooms.csv')


def load_mushrooms(features, encode=False):
    df = pd.read_csv(DATAFILE_PATH, usecols=features+['class'])
    enc = {}
    if encode:
        for col in df:
            encoder = preprocessing.LabelEncoder()
            df[col] = encoder.fit_transform(df[col])
            enc[col] = encoder

        def decode(data, column):
            # Takes in data as array-like. Ex: numpy array
            return enc[column].inverse_transform(data)

        def encode(data, column):
            # Takes in data as pandas.DataFrame
            return enc[column].transform(data[column])

        return df, encode, decode
    else:
        return df
