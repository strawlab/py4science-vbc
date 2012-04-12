#include <stdlib.h>

#include "prime.h"

void calculate_primes(int *data, int kmax)
{
    int i,j,k,n;
    int *p;

    p = calloc(kmax, sizeof(int));

    k = 0; n = 2; j = 0;
    while (k < kmax) {
        i = 0;
        while ((i < k) && (n % p[i] != 0))
            i = i + 1;
        if (i == k) {
            p[k] = n;
            k = k + 1;
            data[j++] = n;
        }
        n += 1;
    }

    free(p);
}
