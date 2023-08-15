from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time


def open_browser(driver):
    driver.get("https://web.whatsapp.com")


def find_chat(driver, contact):
    search_box = driver.find_element(
        by="xpath",
        value='//div[@contenteditable="true"][@data-tab="3"]'
    )
    search_box.clear()
    search_box.send_keys(contact)
    search_box.send_keys(Keys.ENTER)


def send_message(driver, message):
    input_box = driver.find_element(
        by="xpath",
        value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
    )
    input_box.send_keys(message)

    send_button = driver.find_element(
        by="xpath",
        value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'
    )
    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda d: send_button.is_displayed())
    send_button.click()


def send_link(driver, link):
    input_box = driver.find_element(
        by="xpath",
        value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
    )
    input_box.send_keys(link)
    send_button = driver.find_element(
        by="xpath",
        value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'
    )
    time.sleep(5)
    send_button.click()


def close_browser(driver):
    driver.quit()
