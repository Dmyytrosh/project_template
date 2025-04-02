def print_text_to_console(text):
    print(text)


def write_text_to_file(filepath, text):
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(text)