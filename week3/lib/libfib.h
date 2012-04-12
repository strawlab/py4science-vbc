#ifndef _LIBFIB_H_
#define _LIBFIB_H_

typedef struct _ctx ctx_t; 

ctx_t   *fib_new(unsigned int len);

void    fib_free(ctx_t *ctx);

void    fib_double(ctx_t *ctx);

void    fib_print(ctx_t *ctx);

void    fib_fib(ctx_t *ctx);

void    fib_get_data_nulls_out(char **data, int *len);

#endif /* _LIBFIB_H_ */
