#!/usr/bin/env python
import numpy as np
from matplotlib.mlab import csv2rec

# Matplotlib has a nice module for loading CSV files as structured
# arrays.

# Load iris data. See
# http://en.wikipedia.org/wiki/Iris_flower_data_set

arr=csv2rec('iris.csv')

print arr.dtype
print

for row in arr[:5]:
    print row
print

print np.unique(arr['species'])
print

