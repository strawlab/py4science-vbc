#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "libprime.h"
#include "prime.h"

struct _ctx {
    int len;
    int *data;
};

ctx_t *
prime_new(unsigned int len)
{
    ctx_t *ctx = calloc(1,sizeof(ctx_t));
    ctx->len = len < PRIME_MAX ? len : PRIME_MAX;
    ctx->data = calloc(ctx->len, sizeof(int));
    calculate_primes(ctx->data, ctx->len);
    return ctx;
}

void
prime_free(ctx_t *ctx)
{
    free(ctx->data);
    free(ctx);
}

void
prime_print(ctx_t *ctx)
{
    int i;
    for (i = 0; i < ctx->len; i++)
        printf("%d,",ctx->data[i]);
    printf("\n");
}

void
prime_get_data(ctx_t *ctx, int **data, int *len)
{
    int *d = calloc(ctx->len,sizeof(int));
    *len = ctx->len;
    memcpy (d, ctx->data, ctx->len * sizeof(int));
    *data = d;
}

