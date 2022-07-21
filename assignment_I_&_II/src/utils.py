import numpy as np
import os 
import urllib
import pandas as pd


class Utils():
    @staticmethod
    def check_n_clear_data(df):
        if df.isin([np.nan]).any().any():
            print("There is null values in the data! They will be dropped.")
            df.dropna(inplace=True)
        else:
            print("There is no null values in the data!")

        if df.isin([np.inf, -np.inf]).any().any():
            print("There is inf values in the data! They will be dropped.")
            df = df[~df.isin([np.inf, -np.inf]).any(axis=1)]
        else:
            print("There is no inf values in the data!")

        return df

    @staticmethod
    def download_csv_from_url(csv_localpath, csv_urlpath):
        if os.path.isfile(csv_localpath) == False:
            print("Downloading data from url...")
            urllib.request.urlretrieve(csv_urlpath, csv_localpath)
        else:
            print("Data already downloaded!")
        data = pd.read_csv(csv_localpath)
        return data