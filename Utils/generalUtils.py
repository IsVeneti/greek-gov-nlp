import codecs


def string_to_list(string: str, delim: str):
    converted_list = list(string.split(delim))
    return converted_list


def list_for_path():
    # FIXME: list_for_path
    print("FIXME")


def save_to_txt(text: str, filename: str):
    with codecs.open(filename + ".txt", "w", encoding='utf8') as text_file:
        text_file.write(text)
