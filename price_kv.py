import csv

# Чтение данных из файла
input_filename = 'prices.csv'
output_filename = 'processed_prices.csv'

with open(input_filename, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

# Обработка данных
processed_data = []
for row in data:
    if row:  # Проверка на пустую строку
        price_str = row[0].replace('₽/мес.', '').strip()  # Удаление "₽/мес." и лишних пробелов
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