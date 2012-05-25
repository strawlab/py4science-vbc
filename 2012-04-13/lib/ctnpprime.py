import os.path
import numpy as np
import ctypes as ct

lib = ct.cdll.LoadLibrary(os.path.abspath("libprime.so"))
lib.calculate_primes.argtypes = [np.ctypeslib.ndpointer(dtype = np.intc),ct.c_int]
lib.create_primes.restype = ct.POINTER(ct.c_int)
lib.create_primes.argtypes = [ct.c_int]

def primes1(n):
    dest = np.empty(n, dtype=np.intc)
    lib.calculate_primes(dest, n)
    return dest

def primes2(n):
    #as_array() is apparently slower, not in my tests... http://goo.gl/Ia7dB
    data = lib.create_primes(n)
    return np.ctypeslib.as_array(data, shape=(1,n))

def primes3(n):
    data = lib.create_primes(n)
    buf = np.core.multiarray.int_asbuffer(
            ct.addressof(data.contents), n * np.dtype(np.intc).itemsize)
    return np.frombuffer(buf, np.intc)
