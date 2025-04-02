from app.io import input, output


def main():
    """
    Основна функція, яка виконує читання та запис тексту
    """
    text_console = input.get_text_from_console()
    text_file = input.read_text_from_file("data/input.txt")

    try:
        text_pandas = input.read_text_with_pandas("data/input.csv")
    except Exception as e:
        text_pandas = f"Помилка читання CSV-файлу: {e}"

    output.print_text_to_console(text_console)
    output.print_text_to_console(text_file)
    output.print_text_to_console(text_pandas)

    output.write_text_to_file("data/output.txt", f"{text_console}\n{text_file}\n{text_pandas}")


if __name__ == "__main__":
    main()