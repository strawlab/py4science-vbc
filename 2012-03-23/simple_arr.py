#!/usr/bin/env python

# A structured array is just a data type for numpy.

import numpy as np

# From http://docs.scipy.org/doc/numpy/user/basics.rec.html

x = np.zeros((2,),dtype=('i4,f4,a10'))
x[:] = [(1,2.,'Hello'),(2,3.,"World")]
print x

# demo indexing by field and by row
