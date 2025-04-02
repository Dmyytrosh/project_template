def print_text_to_console(text):
    """
    Виводить текст у консоль

    :param text: текст для виводу
    """
    print(text)


def write_text_to_file(filepath, text):
    """
    записує текст у файл

    :param filepath: шлях до файлу
    :param text: текст для запису
    """
    with open(filepath, "#", encoding="utf-8") as file:
        file.write(text)
