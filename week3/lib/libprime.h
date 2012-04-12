#ifndef _LIBPRIME_H_
#define _LIBPRIME_H_

#define PRIME_MAX   10000

typedef struct _ctx ctx_t; 

ctx_t   *prime_new(unsigned int len);

void    prime_free(ctx_t *ctx);

void    prime_double(ctx_t *ctx);

void    prime_print(ctx_t *ctx);

void    prime_prime(ctx_t *ctx);

void    prime_get_data(ctx_t *ctx, int **data, int *len);

#endif /* _LIBPRIME_H_ */
