#!/usr/bin/env python
import numpy as np
from matplotlib.mlab import csv2rec

arr=csv2rec('iris.csv') # see http://en.wikipedia.org/wiki/Iris_flower_data_set

print arr.dtype
print

for row in arr[:5]:
    print row
print

print np.unique(arr['species'])
print

