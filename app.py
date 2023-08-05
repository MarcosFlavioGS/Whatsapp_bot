#!/usr/bin/env python3
from selenium import webdriver
import time
import src.file_utils as file
import src.whatsapp_utils as wp


def initialization_msg():
    print(
        "****************************************\n",
        "Iniciando o programa !\n",
        "Por favor, não use o computador durante a execução.\n",
        "****************************************"
    )


if __name__ == "__main__":
    driver = webdriver.Chrome()  # Or webdriver.Firefox() for Firefox
    message = file.get_message()
    contacts = file.get_contacts()

    initialization_msg()
    time.sleep(5)
    wp.open_browser(driver)
    time.sleep(10)

    for contact in contacts:
        try:
            wp.find_chat(driver, contact)
            time.sleep(1)
            wp.send_message(driver, message)
        except Exception:
            print(
                f"Houve um problema com o contato: {contact}."
            )
        time.sleep(3)

    wp.close_browser(driver)
    input(
        "Programa finalizado !\nPressione qualquer tecla para fechar"
    )
