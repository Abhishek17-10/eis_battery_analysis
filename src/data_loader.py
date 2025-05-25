import pandas as pd
import os

def load_all_csvs(directory):
    data = []
    for file in os.listdir(directory):
        if file.endswith(".csv"):
            path = os.path.join(directory, file)
            df = pd.read_csv(path)
            df['filename'] = file
            data.append(df)
    return pd.concat(data, ignore_index=True)