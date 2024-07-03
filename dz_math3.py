#3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл,
# обработать данные, найти среднюю цену и вывести ее,
# а также сделать гистограмму цен на диваны


import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import matplotlib.pyplot as plt

# Инициализируем браузер
driver = webdriver.Chrome()

# В отдельной переменной указываем сайт, который будем просматривать
url = "https://www.divan.ru/category/divany-i-kresla"

# Открываем веб-страницу
driver.get(url)

# Используем WebDriverWait для ожидания загрузки элементов
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'lsooF')))
except Exception as e:
    print(f"Ошибка ожидания элемента: {e}")
    driver.quit()
    exit()

# Находим все карточки с диванами с помощью названия класса
divans = driver.find_elements(By.CLASS_NAME, 'lsooF')

print(f"Найдено {len(divans)} диванов")

parsed_data = []

# Перебираем коллекцию диванов
for divan in divans:
    try:
       # Находим цену со скидкой
        try:
            discounted_price_element = divan.find_element(By.CSS_SELECTOR, 'div.pY3d2 span[data-testid="price"]')
            discounted_price = discounted_price_element.text
        except Exception as e:
            discounted_price = "N/A"
            print(f"Ошибка при парсинге цены со скидкой: {e}")

        #print(discounted_price)
        parsed_data.append([discounted_price])
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

# Закрываем подключение браузера
driver.quit()

# Записываем данные в CSV файл
with open("divans.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Цена'])
    writer.writerows(parsed_data)

print("Парсинг завершен. Данные сохранены в divans.csv")

#----------------------------------------------------------------
#Преобразуем данные из файла divans.csv из текста в число

# Чтение данных из файла
input_filename = 'divans.csv'
output_filename = 'int_divans.csv'

with open(input_filename, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

# Обработка данных
processed_data = []
for row in data:
    if row:  # Проверка на пустую строку
        price_str = row[0].replace('руб.', '').strip()  # Удаление "₽/мес." и лишних пробелов
        try:
            price_num = int(price_str.replace(' ', ''))  # Преобразование строки в число (удаление пробелов)
            processed_data.append([price_num])
        except ValueError:
            print(f"Не удалось преобразовать значение '{price_str}' в число")

# Сохранение обработанных данных обратно в CSV
with open(output_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Цена'])  # Запись заголовка
    writer.writerows(processed_data)

print("Обработка завершена, данные сохранены в", output_filename)

# обработать данные, найти среднюю цену и вывести ее,
# также сделать гистограмму цен на диван

# Чтение данных из CSV-файла
df = pd.read_csv(output_filename)

# Вычисление средней цены
average_price = df['Цена'].mean()
print(f'Средняя цена: {average_price}')

# Построение гистограммы цен
plt.hist(df['Цена'], bins=30, edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

# Отображение гистограммы
plt.show()


