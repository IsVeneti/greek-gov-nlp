def replace_newline_with_space_list(textList: list):
    print("Replacing newline with space in text dataset...")
    replaced_list = []
    for element in textList:
        replaced_list.append(element.replace('\n', ' '))
    return replaced_list


def replace_newline_with_space(text: str):
    print("Replacing newline with space in text dataset...")
    replaced_text = text.replace('\n', ' ')
    return replaced_text
