#!/usr/bin/env python
import numpy as np
from matplotlib.mlab import csv2rec
import h5py

# read a .csv file
arr=csv2rec('iris.csv')

# write it as an .h5 file
with h5py.File('iris.h5','w') as f:
    f.create_dataset( 'iris', data=arr )

# read the new .h5 file
with h5py.File('iris.h5','r') as f2:
    arr2 = f2['iris'][:]

print 'arr'
print arr[:5]
print

print 'arr2'
print arr2[:5]
print
