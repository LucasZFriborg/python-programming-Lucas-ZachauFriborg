import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# läser in datan en gång
data = pd.read_csv("Labs/Labb 3/data/unlabelled_data.csv", header = None)    # (header = None) = filen har inte rubriker

# definierar en funktion som ritar linjen
def plot_data_with_line(k, m):
    plt.scatter(data[0], data[1])    # ritar datapunkterna som spridning i diagrammet
    x_line = np.linspace(-5, 5, 100)    # skapar x-värden
    y_line = k * x_line + m    # räknar ut y-värden
    plt.plot(x_line, y_line, color = 'red')    # ritar linjen
    plt.axhline(0, color = 'gray', linestyle = '--')    # 
    plt.axvline(0, color = 'gray', linestyle = '--')
    plt.title(f'k = {k}, m = {m}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

plot_data_with_line(-1.5, 0.1)

def classify_point(x, y, k, m):
    line_y = k * x + m
    if y > line_y:
        return 1
    else:
        return 0

classify_point(1, 2, -1.5, 0.1)
classify_point(-2, -3, -1.5, 0.1)