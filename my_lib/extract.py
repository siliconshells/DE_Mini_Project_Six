"""
Extract data from a url and save as a file
"""

import requests
import pandas as pd


def extract(
    url: str,
    file_name: str,
):
    """ "Extract a url to a file path"""
    file_path = "data/" + file_name
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return "Extract Successful"


def extract(url: str, file_name: str, column_contains: tuple):
    """ "Extract a url to a file path"""
    file_path = "data/" + file_name
    df = pd.read_csv(url)
    df = df[df[column_contains[0]].str.contains(column_contains[1])]
    df.to_csv(file_path)
    return "Extract Successful"
