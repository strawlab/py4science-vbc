cdef extern from "libprime.h":
    ctypedef struct ctx_t:
        pass
    ctx_t *prime_new(unsigned int len)
    void prime_free(ctx_t *ctx)
    void prime_print(ctx_t *ctx)

cdef class Prime:
    cdef ctx_t *_ctx
    def __cinit__(self, len):
        self._ctx = prime_new(len)
    def __dealloc__(self):
        prime_free(self._ctx)
    def _print(self):
        prime_print(self._ctx)
