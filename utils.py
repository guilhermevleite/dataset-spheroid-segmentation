import pandas as pd


def open_csv(path: str):

    try:
        file = pd.read_csv(path)
    except:
        file = {}

    return file
