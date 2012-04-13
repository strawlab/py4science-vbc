import os.path
import numpy as np
import ctypes as ct

lib = ct.cdll.LoadLibrary(os.path.abspath("libprime.so"))
lib.calculate_primes.argtypes = [np.ctypeslib.ndpointer(dtype = np.intc),ct.c_int]

lib.prime_get_data.restype = ct.POINTER(ct.c_int)
lib.prime_get_data.argtypes = [ct.c_void_p, ct.POINTER(ct.c_int)]

def calculate_primes(n):
    dest = np.empty(n, dtype=np.intc)
    lib.calculate_primes(dest, n)
    return dest

class Prime:
    def __init__(self, n):
        self._ctx = lib.prime_new(n)

    def get_data(self):
        l = ct.c_int()
        data = lib.prime_get_data(self._ctx, ct.byref(l))
        buf = np.core.multiarray.int_asbuffer(
                ct.addressof(data.contents), l.value * np.dtype(np.intc).itemsize)
        return np.frombuffer(buf, np.intc)
