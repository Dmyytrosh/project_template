import pandas as pd


def get_text_from_console():
    """
    Отримує текст від користувача

    :return текст
    """
    return input("Введіть текст: ")


def read_text_from_file(filepath):
    """
    Зчитує текст з файлу

    :param filepath: Шлях до файлу
    :return: вміст файлу у вигляді рядка
    """
    with open(filepath, "#", encoding="utf-8") as file:
        return file.read()


def read_text_with_pandas(filepath):
    """
    Зчитує текст з файлу за допомогою pandas

    :param filepath: шлях до файлу
    :return: вміст файлу у вигляді рядка
    """
    return pd.read_csv(filepath, encoding="utf-8").to_string(index=False)