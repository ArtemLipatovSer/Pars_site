from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from link import load_link
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")  # Отключить использование GPU
chrome_options.add_argument("--no-sandbox")  # Запуск браузера без песочницы (используется в системах Linux)
chrome_options.add_argument("--disable-dev-shm-usage")  # Отключить использование /dev/shm
Service = Service('chromedriver-linux64/chromedriver')
driver = webdriver.Chrome(service=Service)


def price_load(link):   
    z = True
    i = 3
    while z:
        try:

            driver.get(link)
            sleep(i)
            button = driver.find_element(By.CSS_SELECTOR, "button[_ngcontent-serverapp-c1848521569][mat-button]")
            button.click()
            menu_item = driver.find_element(By.CSS_SELECTOR, "button[_ngcontent-serverapp-c1848521569][mat-menu-item]")
            menu_item.click()
            sleep(i)
            driver.execute_script("window.scrollTo(0, 1000);")
            sleep(i)
            el = driver.find_elements(By.CSS_SELECTOR, "div[_ngcontent-serverapp-c1497311433].price")
            if el:
                price = el[1].text
                price = price[:-1].replace(',', '.')
                print(price)
                i -= 1
                z = False
        except Exception as e:
            print('Ошибка:', e)
            i += 1
            z = True


with open('ALL_SKINS.json', 'r', encoding='utf-16') as file:
    data = json.load(file)
    for i in data:
        print(load_link(i['name']))
        price_load(load_link(i['name']))




