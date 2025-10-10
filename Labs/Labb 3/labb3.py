import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# läser in datan och ger kolumnerna namnen 'x' och 'y'
data = pd.read_csv("Labs/Labb 3/data/unlabelled_data.csv", header = None, names = ['x', 'y'])

# linjens lutning och skärningspunkt justerade så att linjen delar punkterna jämnt
k = -1.5
m = 0.4

# avgör om en punkt ligger ovanför eller under linjen, 1 eller 0
def classify_point(x, y, k, m):
    line_y = k * x + m
    return 1 if y > line_y else 0

labels = []
for x, y in zip(data['x'], data['y']):    # itererar över x och y från datan samtidigt med zip
    label = classify_point(x, y, k, m)
    labels.append(label)
data['label'] = labels

# kontrollerar om filen redan finns för att inte skapa en ny fil varje gång programmet körs
if not os.path.exists("Labs/Labb 3/data/labelled_data.csv"):
    data.to_csv("Labs/Labb 3/data/labelled_data.csv", index = False)   # tar inte med radnumret eftersom datan redan har x, y och label

# delar upp datan i två klasser inför plottningen
class0 = data[data['label'] == 0]
class1 = data[data['label'] == 1]

# skapar linjen y = kx + m
x_line = np.linspace(-5, 5, 100)
y_line = k * x_line + m

# visualisering av punkterna och linjen
plt.scatter(class0['x'], class0['y'], color = 'blue', label = 'Class 0')
plt.scatter(class1['x'], class1['y'], color = 'orange', label = 'Class 1')
plt.plot(x_line, y_line, color = 'red', label = 'Separating line')
plt.title('Classification of points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()