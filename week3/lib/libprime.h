#ifndef _LIBPRIME_H_
#define _LIBPRIME_H_

#define PRIME_MAX   10000

typedef struct _ctx ctx_t; 

ctx_t   *prime_new(unsigned int len);
void    prime_free(ctx_t *ctx);
void    prime_print(ctx_t *ctx);
int     *prime_get_data(ctx_t *ctx, int *len);

void    calculate_primes(int *data, int kmax);
int     *create_primes(int kmax);

#endif /* _LIBPRIME_H_ */
