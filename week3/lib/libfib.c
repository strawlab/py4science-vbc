#include <stdlib.h>
#include <stdio.h>

#include "libfib.h"

struct _ctx {
    int len;
    char *data;
};

ctx_t *
fib_new(unsigned int len)
{
    ctx_t *ctx = calloc(1,sizeof(ctx_t));
    ctx->len = ((len % 2) == 0) ? len : len + 1;
    ctx->data = calloc(ctx->len, sizeof(char));
    return ctx;
}

void
fib_free(ctx_t *ctx)
{
    free(ctx->data);
    free(ctx);
}

void
fib_double(ctx_t *ctx)
{
    int i;
    for (i=0; i<ctx->len; i++)
        ctx->data[i] *= 2;
}

void
fib_fib(ctx_t *ctx)
{
    int i;
    
    ctx->data[0] = 0;
    ctx->data[1] = 1;

    for(i = 2; i < ctx->len; i++)
        ctx->data[i] = ctx->data[i-1] + ctx->data[i-2];
}

void
fib_print(ctx_t *ctx)
{
    int i;
    for (i = 0; i < ctx->len; i++)
        printf("%x,",ctx->data[i]);
    printf("\n");
}


void
fib_get_data_nulls_out(char **data, int *len)
{
    *len = 5;
    char *d = malloc(5);
    d[0] = 'a';
    d[1] = 'b';
    d[2] = '\0';
    d[3] = 'c';
    d[4] = '\0';
    *data = d;
}
