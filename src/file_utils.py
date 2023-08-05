def get_message():
    with open("message.txt", 'r', encoding="UTF-8") as file:
        message = [i.strip() for i in file]
    return message


def get_contacts():
    with open("contatos.txt", 'r') as contacts:
        contacts = [i.strip() for i in contacts]
    return contacts
