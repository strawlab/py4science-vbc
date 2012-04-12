import os.path
from ctypes import *

lib = cdll.LoadLibrary(os.path.abspath("libprime.so"))

class Prime:
    def __init__(self, n):
        self._ctx = lib.prime_new(n)

    def _print(self):
        lib.prime_print(self._ctx)
