import pandas as pd
import os

def load_dataset():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "..", "data", "raw", "games.csv")

    df = pd.read_csv(file_path)
    df = df.dropna()
    df = df[df["Positive"] + df["Negative"] > 0]

    return df