import matplotlib.pyplot as plt
import numpy as np

# Данные из таблицы
x = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
y_1 = np.array([1.0, 1.125, 1.561, 2.516, 4.11, 8.0])  # Точное измерение
y_2 = np.array([1.0, 1.0, 1.24, 1.794, 2.857, 4.79])  # Метод Эйлера
y_3 = np.array([1.0, 1.12, 1.538, 2.445, 4.23, 7.589])  # Модифицированный метод Эйлера
y_4 = np.array([1.0, 1.125, 1.561, 2.516, 4.411, 7.999])  # Метод Рунге-Кутта

# Создание графика с тёмным фоном
plt.style.use('dark_background')

# Построение графиков
plt.plot(x, y_1, marker='o', color='lime', label='Точное измерение (y_1)')
plt.plot(x, y_2, marker='o', color='cyan', label='Метод Эйлера (y_2)')
plt.plot(x, y_3, marker='o', color='magenta', label='Модифицированный метод Эйлера (y_3)')
plt.plot(x, y_4, marker='o', color='yellow', label='Метод Рунге-Кутта (y_4)')

# Добавление значений y рядом с точками
for xi, yi in zip(x, y_1):
    plt.text(xi, yi, f'{yi:.2f}', fontsize=8, ha='right', va='bottom', color='white')
for xi, yi in zip(x, y_2):
    plt.text(xi, yi, f'{yi:.2f}', fontsize=8, ha='left', va='top', color='white')
for xi, yi in zip(x, y_3):
    plt.text(xi, yi, f'{yi:.2f}', fontsize=8, ha='right', va='top', color='white')
for xi, yi in zip(x, y_4):
    plt.text(xi, yi, f'{yi:.2f}', fontsize=8, ha='left', va='bottom', color='white')

# Добавление заголовка и подписей осей
plt.title('Сравнение точного решения и приближенных решений исходного дифференциального уравнений:')
plt.xlabel('x')
plt.ylabel('y')

# Добавление сетки
plt.grid(True, linestyle='--', alpha=0.7)

# Добавление легенды
plt.legend()

# Отображение графика
plt.show()
