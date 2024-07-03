import pandas as pd
import matplotlib.pyplot as plt
import csv

# Загрузка данных из CSV файла
file_path='processed_prices.csv'
data = pd.read_csv(file_path)
prices = data['Цена']

plt.hist(data['Цена'], bins=10, color='blue', alpha=0.7)
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Количество')

plt.grid(True)
plt.show()





