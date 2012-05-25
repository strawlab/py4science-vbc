import os.path
import ctypes as ct
import ctypes.util

lib = ct.cdll.LoadLibrary(os.path.abspath("libprime.so"))
lib.prime_get_data.restype = ct.POINTER(ct.c_int)
lib.prime_get_data.argtypes = [ct.c_void_p, ct.POINTER(ct.c_int)]

clib = ct.cdll.LoadLibrary(ctypes.util.find_library("c"))

class Prime:
    def __init__(self, n):
        self._ctx = lib.prime_new(n)

    def _print(self):
        lib.prime_print(self._ctx)

    def get_data(self):
        l = ct.c_int()
        data = lib.prime_get_data(self._ctx, ct.byref(l))
        #note the extra data copy here
        pydata = [data[i] for i in range(l.value)]
        #free the old data using c-library free func
        clib.free(data)
        return pydata

