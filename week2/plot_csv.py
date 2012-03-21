#!/usr/bin/env python
import numpy as np
from matplotlib.mlab import csv2rec
import matplotlib.pyplot as plt

arr=csv2rec('iris.csv') # see http://en.wikipedia.org/wiki/Iris_flower_data_set

all_species = np.unique(arr['species'])
for species in all_species:
    cond = arr['species']==species
    xax = 'sepal_length'
    yax = 'sepal_width'
    plt.plot( arr[xax][cond], arr[yax][cond], 'o', label=species )
    plt.xlabel(xax)
    plt.ylabel(yax)
plt.legend()
plt.show()
