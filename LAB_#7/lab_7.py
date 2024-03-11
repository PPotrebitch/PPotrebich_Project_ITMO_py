from sin_1 import animSin
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import time


def show_time():
    box_1 = [random.random() for _ in range(1000001)]
    box_2 = [random.random() for _ in range(1000001)]
    Array_1 = np.array(box_1)
    Array_2 = np.array(box_2)

    stert_time = time.perf_counter()
    result_box = [box_1[p] * box_2[p] for p in range(len(box_1))]
    end_time = time.perf_counter()
    print("Execution time multiplication of lists:", end_time - stert_time)
    
    stert_time = time.perf_counter()
    result_Array = np.multiply(Array_1, Array_2) 
    end_time = time.perf_counter()
    print("Execution time multiplication of arrays NumPy:", end_time - stert_time)

def histograms():
    data = pd.read_csv('data2.csv')
    print("Standard deviation: ", np.std(data['Solids']))
    plt.hist(data["Solids"], bins=50, label="histogram for task 2", )
    plt.xlabel('Дата')
    plt.ylabel('Цена')
    plt.title('Обновляемые графики в matplotlib')
    plt.show()
    ''''
    n, bins, patches = plt.hist(data["Solids"], bins=16, facecolor='green')
    #bins = np.delete(bins, len(bins)-1, 0)
    he = np.histogram(data["Solids"], bins=bins, density=True)[0]
    print(len(he))
    for i in range(len(he)):
        he[i] = he[i] / n[i]
    print(he)
    print(bins)
    print(len(bins), type(bins))

    plt.plot(he, bins,  color='red', linewidth=2, label='Эквализированная гистограмма')
    plt.xlabel('Значения')
    plt.ylabel('Плотность')
    plt.title('Гистограмма и эквализированная гистограмма')
    plt.show()
    '''
def plot3D():
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
    x = np.linspace(-np.pi, np.pi, 100)
    y = 1/x
    z = np.sin(x)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(x, y, z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Plot')
    plt.show()


if __name__ == "__main__":
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
    animSin()
    show_time()
    plot3D()
    histograms()

