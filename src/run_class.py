from src.file_utils import get_content, get_message
import json


class Run:
    def __init__(self):
        self.message = ""
        self.site = ""
        self.contacts = []
        self.restart = True
        self.last_contact = ""
        self.sleep_link = 5
        self.sleep_contact = 3

def get_config(run):
        with open('config.json', 'r') as json_file:
            # 2. Parse the JSON data from the file
            data = json.load(json_file)

        run.contacts = get_content(data["files"]["contatos"])
        run.message = get_message(data["files"]["mensagem"])
        run.site = get_content(data["files"]["link"])
        run.restart = data.get("recomeçar")
        run.last_contact = data.get("ultimo contato")
        run.sleep_link = data.get("tempo para link")
        run.sleep_contact = data.get("tempo entre contatos")

        return data
