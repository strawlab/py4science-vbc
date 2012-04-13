#ifndef _LIBPRIME_H_
#define _LIBPRIME_H_

#define PRIME_MAX   10000

/* A library for computing sequences of primes */

typedef struct _ctx ctx_t; 

ctx_t   *prime_new(unsigned int len);
void    prime_free(ctx_t *ctx);
void    prime_print(ctx_t *ctx);
/* return new array of prime numbers */
int     *prime_get_data(ctx_t *ctx, int *len);

/* fill array with prime numbers */
void    calculate_primes(int *data, int kmax);
/* return new array of prime numbers */
int     *create_primes(int kmax);

#endif /* _LIBPRIME_H_ */
