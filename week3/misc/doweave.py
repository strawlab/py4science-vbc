import time
from numpy import *

import weavedemo

N_array = 10000
N_py = 200
N_c = 10000

ratio = float(N_c) / N_py

arr = [0]*N_array
t1 = time.time()
for i in xrange(N_py):
    weavedemo.ramp(arr, N_array, 0.0, 1.0)
t2 = time.time()
py_time = (t2 - t1) * ratio
print 'python (seconds*ratio):', py_time
print 'arr[500]:', arr[500]

arr1 = array([0]*N_array,float)
# First call compiles function or loads from cache.
# I'm not including this in the timing.
weavedemo.ramp_numeric1(arr1, 0.0, 1.0)
t1 = time.time()
for i in xrange(N_c):
    weavedemo.ramp_numeric1(arr1, 0.0, 1.0)
t2 = time.time()
c_time = (t2 - t1)
print 'compiled numeric1 (seconds, speed up):', c_time, py_time/ c_time
print 'arr[500]:', arr1[500]
