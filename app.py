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
    message = file.get_content("message.txt")
    contacts = file.get_content("contatos.txt")
    site = file.get_content("link.txt")

    initialization_msg()
    time.sleep(5)
    wp.open_browser(driver)
    time.sleep(20)

    for contact in contacts:
        try:
            wp.find_chat(driver, contact)
            time.sleep(1)
            wp.send_message(driver, message)
            for line in site:
                wp.send_link(driver, line)
        except Exception:
            print(
                f"Houve um problema com o contato: {contact}."
            )
        time.sleep(3)

    wp.close_browser(driver)
    input(
        "Programa finalizado !\nPressione qualquer tecla para fechar"
    )
