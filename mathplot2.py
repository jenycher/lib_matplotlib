#Гистограмма
import matplotlib.pyplot as plt

data=[1,2,2,3,4,4,4,5,6,6,6,6,6,6]

plt.hist(data,bins=6)

#3. Кастомизируем график, чтобы было понятно, где что. Даём графику название:
plt.title("Пример гистограммы")

#4. Даём названия осям графика:

plt.xlabel("x ось")
plt.ylabel("y ось")

#5. Прописываем функцию для того, чтобы показать график:
plt.show()