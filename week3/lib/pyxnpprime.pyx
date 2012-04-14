cimport numpy as np

np.import_array()

cdef extern from "libprime.h":
    int     *create_primes(int kmax)

def primes(int kmax):
    cdef np.npy_intp shape[1]
    cdef int* arr_ptr = create_primes(kmax)
    shape[0] = kmax
    ndarray = np.PyArray_SimpleNewFromData(1, shape, np.NPY_INT, <void*>arr_ptr)
    #numpy owns the memory (assumes it was malloc'd), and will free() it for us
    np.PyArray_UpdateFlags(ndarray, ndarray.flags.num | np.NPY_OWNDATA)
    return ndarray
