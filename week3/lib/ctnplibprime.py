import os.path
import numpy as np
import ctypes as ct

lib = ct.cdll.LoadLibrary(os.path.abspath("libprime.so"))

class Prime:
    def __init__(self, n):
        self._ctx = _lib.prime_new(n)

    def get_data(self):
        pass
