cdef extern from "libfib.h":
    ctypedef struct ctx_t:
        pass
    ctx_t *fib_new(unsigned int len)
    void fib_free(ctx_t *ctx)
    void fib_double(ctx_t *ctx)
    void fib_print(ctx_t *ctx)
    void fib_fib(ctx_t *ctx)

cdef class Fib:
    cdef ctx_t *_ctx
    def __cinit__(self, len):
        self._ctx = fib_new(len)
    def __dealloc__(self):
        fib_free(self._ctx)
    def fib(self):
        fib_fib(self._ctx)
    def double(self):
        fib_double(self._ctx)
    def _print(self):
        fib_print(self._ctx)
