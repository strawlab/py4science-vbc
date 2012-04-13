cimport numpy as np

cdef extern from "libprime.h":
    void    calculate_primes(int *data, int kmax)
    int     *create_primes(int kmax)

def primes(int kmax):
    cdef np.npy_intp* shape = [0]
    cdef int* arr_ptr

    arr_ptr = create_primes(kmax)
    shape[0] = kmax

    return np.PyArray_SimpleNewFromData(1, shape, np.NPY_INT, <void*>arr_ptr)
