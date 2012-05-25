#!/usr/bin/env python
import h5py
import pandas

# read the .h5 file
with h5py.File('iris.h5','r') as f2:
    arr = f2['iris'][:]

df = pandas.DataFrame(arr)
print df.groupby('species').mean()
