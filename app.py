#!/usr/bin/env python3
from selenium import webdriver
import time
import re
import src.whatsapp_utils as wp
from src.run_class import Run, get_config, update_json


def initialization_msg():
    print(
        "****************************************\n",
        "Iniciando o programa !\n",
        "Por favor, não use o computador durante a execução.\n",
        "****************************************"
    )


if __name__ == "__main__":
    driver = webdriver.Chrome()  # Or webdriver.Firefox() for Firefox
    run = Run()
    json_data = get_config(run)

    initialization_msg()
    time.sleep(5)
    wp.open_browser(driver)
    time.sleep(20)

    for contact in run.contacts:
        message = re.sub(r'PESSOA', contact, str(run.message))

        try:
            wp.find_chat(driver, contact)
            time.sleep(1)
            wp.send_message(driver, message)
            for line in run.site:
                wp.send_link(driver, line, run.sleep_link)
        except Exception:
            print(
                f"Houve um problema com o contato: {contact}."
            )
        run.last_contact = contact
        update_json(json_data, "ultimo contato", contact)
        time.sleep(run.sleep_contact)

    wp.close_browser(driver)
    input(
        "Programa finalizado !\nPressione qualquer tecla para fechar"
    )
