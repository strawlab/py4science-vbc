cimport numpy as np
import numpy as np

#something is not working here...

cdef extern from "libprime.h":
    void    calculate_primes(int *data, int kmax)
    int     *create_primes(int kmax)

def primes(int kmax):
    cdef np.npy_intp* shape = [0]
    cdef int* arr_ptr = create_primes(kmax)

    shape[0] = kmax
    return np.PyArray_SimpleNewFromData(1, shape, np.NPY_INT, <void*>arr_ptr)

def primes2(int kmax):
    cdef np.ndarray[np.int, ndim=1] r = np.zeros((kmax,), dtype=np.int)
    calculate_primes(<int *>r.data, kmax)
    return r
