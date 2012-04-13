import os.path
from ctypes import *

_lib = cdll.LoadLibrary(os.path.abspath("libprime.so"))

class Prime:
    def __init__(self, n):
        self._ctx = _lib.prime_new(n)

    def _print(self):
        _lib.prime_print(self._ctx)

    def get_data(self):
        func = _lib.prime_get_data
        func.restype = POINTER(c_int)
        func.argtypes = [c_void_p, POINTER(c_int)]

        l = c_int()
        data = func(self._ctx, byref(l))

        return [data[i] for i in range(l.value)]

