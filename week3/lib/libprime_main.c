#include <stdio.h>

#include "libprime.h"

int main (void)
{
    ctx_t *ctx = prime_new(2000);
    prime_print(ctx);
    prime_free(ctx);
    return 0;
}
