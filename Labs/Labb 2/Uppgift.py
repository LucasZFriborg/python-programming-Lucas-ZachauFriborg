import numpy as np
import matplotlib.pyplot as plt
import random



with open('Labs/Labb 2/datapoints.txt', 'r') as datafile:
    data = datafile.read().splitlines()
data.pop(0)
print(data)
