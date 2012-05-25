cimport numpy as c_np
c_np.import_array()

import numpy as np

cdef extern from "libprime.h":
    int     *create_primes(int kmax)
    void    calculate_primes(int *data, int kmax)

def primes1(int kmax):
    cdef c_np.npy_intp shape[1]
    cdef int* arr_ptr = create_primes(kmax)
    shape[0] = kmax
    ndarray = c_np.PyArray_SimpleNewFromData(1, shape, c_np.NPY_INT, <void*>arr_ptr)
    #numpy owns the memory and will free() it for us. There is an implicit
    #assumption that it was malloc'd, so be wary of changes to mem allocation function
    c_np.PyArray_UpdateFlags(ndarray, ndarray.flags.num | c_np.NPY_OWNDATA)
    return ndarray

def primes2(int kmax):
    cdef c_np.ndarray[c_np.int_t, ndim=1, mode='c'] d
    #ascontiguousarray might incur an extra copy, depending on the alignment
    #and the system. np.zeros is also executed in python, so it might be slower than C
    d = np.ascontiguousarray(np.zeros((kmax,), np.int), dtype=np.int)
    calculate_primes(<int*>d.data, kmax)
    return d



