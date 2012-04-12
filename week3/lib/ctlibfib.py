import os.path
from ctypes import *

lib = cdll.LoadLibrary(os.path.abspath("libfib.so"))

class Fib:
    def __init__(self):
        self._ctx = lib.fib_new(5)

    def _print(self):
        lib.fib_print(self._ctx)
