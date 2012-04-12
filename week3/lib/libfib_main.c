#include <stdio.h>

#include "libfib.h"

int main (void)
{
    ctx_t *ctx = fib_new(5);

    fib_fib(ctx);
    fib_print(ctx);
    fib_double(ctx);
    fib_print(ctx);

    fib_free(ctx);

    return 0;
}
