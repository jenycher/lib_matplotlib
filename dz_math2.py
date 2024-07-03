#2. Построй диаграмму рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand`.
#import numpy as np
#random_array = np.random.rand(5)  # массив из 5 случайных чисел
#print(random_array)

import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 100  # Количество образцов
x = np.random.rand(num_samples)
y = np.random.rand(num_samples)

# Построение диаграммы рассеяния
plt.scatter(x, y, c='blue', alpha=0.5, edgecolors='w', linewidths=0.5)

# Добавление заголовка и меток осей
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X')
plt.ylabel('Y')

# Отображение диаграммы рассеяния
plt.show()