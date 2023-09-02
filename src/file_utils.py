def get_content(path):
    with open(path, 'r', encoding="UTF-8") as file:
        content = [i.strip() for i in file]
    return content


def get_message(path):
    with open(path, 'r', encoding="UTF-8") as file:
        lines = [i.strip() for i in file]
        content = "\n".join(lines)
    return content
