#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def initialization_msg():
    print(
        "****************************************\n",
        "Iniciando o programa !\n",
        "Por favor, não use o computador durante a execução.\n",
        "****************************************"
    )

def open_browser(driver):
    driver.get("https://web.whatsapp.com")

def find_chat(driver, contact):
    search_box = driver.find_element(by="xpath", value='//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(contact)
    search_box.send_keys(Keys.ENTER)

def send_message(driver, message):
    input_box = driver.find_element(by="xpath", value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')

    input_box.clear()
    input_box.send_keys(message)

    send_button = driver.find_element(by="xpath", value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
    time.sleep(3)
    send_button.click()

def close_browser(driver):
    driver.quit()

def get_message():
    with open("message.txt", 'r', encoding = "UTF-8") as file:
        message = [i.strip() for i in file]
    return message

def get_contacts():
    with open("contatos.txt", 'r') as contacts:
        contacts = [i.strip() for i in contacts]
    return contacts

if __name__ == "__main__":
    driver = webdriver.Chrome()  # Or webdriver.Firefox() for Firefox
    message = get_message()
    contacts = get_contacts()

    initialization_msg()
    time.sleep(5)
    open_browser(driver)
    time.sleep(10)
    for contact in contacts:
        try:
            find_chat(driver, contact)
            time.sleep(2)
            send_message(driver, message)
        except:
            print(f"Houve um problema com o contato: {contact}.")
        time.sleep(3)

    input("Programa finalizado !\nPressione qualquer tecla para fechar")
    close_browser(driver)
