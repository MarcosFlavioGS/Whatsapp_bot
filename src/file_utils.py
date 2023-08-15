def get_message():
    with open("message.txt", 'r', encoding="UTF-8") as file:
        message = [i.strip() for i in file]
    return message


def get_contacts():
    with open("contatos.txt", 'r', encoding="UTF-8") as contacts:
        contacts = [i.strip() for i in contacts]
    return contacts


def get_link():
    with open("link.txt", "r", encoding="UTF-8") as file:
        site = [i.strip() for i in file]
    return site
