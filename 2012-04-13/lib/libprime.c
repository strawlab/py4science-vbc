#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "libprime.h"

struct _ctx {
    int len;
    int *data;
};

ctx_t *
prime_new(unsigned int len)
{
    ctx_t *ctx = calloc(1,sizeof(ctx_t));
    ctx->len = len < PRIME_MAX ? len : PRIME_MAX;
    ctx->data = create_primes(ctx->len);
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

int *
prime_get_data(ctx_t *ctx, int *len)
{
    int *d = calloc(ctx->len,sizeof(int));
    *len = ctx->len;
    memcpy (d, ctx->data, ctx->len * sizeof(int));
    return d;
}

void
calculate_primes(int *data, int kmax)
{
    int i,k,n;

    k = 0; n = 2;
    while (k < kmax) {
        i = 0;
        while ((i < k) && (n % data[i] != 0))
            i = i + 1;
        if (i == k) {
            data[k] = n;
            k = k + 1;
        }
        n += 1;
    }

}

int *
create_primes(int kmax)
{
    int i,k,n;
    int *p = calloc(kmax, sizeof(int));

    k = 0; n = 2;
    while (k < kmax) {
        i = 0;
        while ((i < k) && (n % p[i] != 0))
            i = i + 1;
        if (i == k) {
            p[k] = n;
            k = k + 1;
        }
        n += 1;
    }

    return p;
}

