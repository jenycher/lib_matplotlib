#Создадим небольшой кейс с использованием построения графиков.

#Есть сайт “циан”, на котором мы можем снимать или покупать квартиры. Нам нужно спарсить цены и составить график этих цен.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv
# Инициализация драйвера
driver = webdriver.Chrome()

# Открытие страницы
driver.get('https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/')

# Ожидание загрузки страницы
time.sleep(5)

try:
    # Поиск элементов с ценой
    prices = driver.find_elements(By.XPATH,
                                  "//span[@data-mark='MainPrice']/span")

    # Открытие файла для записи
    with open('prices.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Цена'])  # Заголовок для CSV файла

        # Запись цен в файл
        for price in prices:
            writer.writerow([price.text])
finally:
    # Закрытие браузера
    driver.quit()