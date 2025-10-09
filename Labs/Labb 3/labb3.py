import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

data = pd.read_csv("Labs/Labb 3/data/unlabelled_data.csv", header = None, names = ['x', 'y'])

k = -1.5    # linjens lutning
m = 0.1    # linjens skärningspunkt

def plot_data_with_line(k, m):    # definierar en funktion som ritar linjen
    plt.scatter(data['x'], data['y'])    # ritar datapunkterna som spridning i diagrammet
    x_line = np.linspace(-5, 5, 100)    # skapar x-värden
    y_line = k * x_line + m    # räknar ut y-värden
    plt.plot(x_line, y_line, color = 'red')    # ritar linjen
    plt.title(f'k = {k}, m = {m}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def classify_point(x, y, k, m):    # returnerar 1 om punkten ligger över linjen, annars 0
    line_y = k * x + m
    if y > line_y:
        return 1
    else:
        return 0

labels = []
for x, y in zip(data['x'], data['y']):
    label = classify_point(x, y, k, m)
    labels.append(label)

data['label'] = labels

if not os.path.exists("Labs/Labb 3/data/labelled_data.csv"):    # kollar om filen redan finns för att inte skapa en ny fil varje gång programmet körs
    data.to_csv("Labs/Labb 3/data/labelled_data.csv", index = False)

class0 = data[data['label'] == 0]
class1 = data[data['label'] == 1]

plt.scatter(class0['x'], class0['y'], color = 'blue', label = 'Class 0')
plt.scatter(class1['x'], class1['y'], color = 'orange', label = 'Class 1')

x_line = np.linspace(-5, 5, 100)
y_line = k * x_line + m
plt.plot(x_line, y_line, color = 'red', label = 'Separating line')

plt.title('Classification of points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()