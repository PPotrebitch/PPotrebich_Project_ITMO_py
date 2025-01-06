import matplotlib.pyplot as plt
import numpy as np


# Данные из таблицы
x = np.array([0.0, 0.1, 0.2, 0.3])
y_1 = np.array([2.0, 2.261964, 2.551379, 2.871122])  # Точное измерение
y_2 = np.array([2.0, 2.210345, 2.442834, 2.699816])  # Метод Рунге-Кутта

# Создание графика с тёмным фоном
plt.style.use('dark_background')

plt.plot(x, y_1, marker='o', color='red', label='Точное измерение (y_1)')
plt.plot(x, y_2, marker='o', color='yellow', label='Метод Рунге-Кутта (y_2)')


# Добавление значений y рядом с точками

for xi, yi in zip(x, y_1):
    plt.text(xi, yi, f'{yi:.2f}', fontsize=12, ha='right', va='bottom', color='blue')
for xi, yi in zip(x, y_2):
    plt.text(xi, yi, f'{yi:.2f}', fontsize=12, ha='left', va='top', color='orange')

# Добавление заголовка и подписей осей
plt.title('Сравнение точного решения и метода Рунге-Кутта дифференциального уравнения второго порядка:')
plt.xlabel('x')
plt.ylabel('y')

# Добавление сетки
plt.grid(True, linestyle='--', alpha=0.7)

# Добавление легенды
plt.legend()

# Отображение графика
plt.show()
