import pandas as pd


def get_text_from_console():
    return input("Введіть текст: ")


def read_text_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def read_text_with_pandas(filepath):
    return pd.read_csv(filepath, encoding="utf-8").to_string(index=False)