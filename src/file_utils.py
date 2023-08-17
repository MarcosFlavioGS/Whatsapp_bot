def get_content(path):
    with open(path, 'r', encoding="UTF-8") as file:
        content = [i.strip() for i in file]
    return content
