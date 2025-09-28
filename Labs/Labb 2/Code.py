import numpy as np
import matplotlib.pyplot as plt


with open('datapoints.txt', 'r') as datafile:
    data = datafile.read().splitlines()

data.pop(0)