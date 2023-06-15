import pandas as pd
from pathlib import Path


def open_csv(path: str):

    try:
        file = pd.read_csv(path)
    except:
        file = {}

    return file


def create_dir(path):
    if not path.exists():
        path.mkdir(parents=True)
