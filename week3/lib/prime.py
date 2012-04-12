def primes(kmax):
    if kmax > 100000:
        kmax = 100000
    k = 0
    n = 2
    j = 0
    result = [0] * kmax
    p = [0] * kmax
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result[j] = n; j = j + 1
        n = n + 1
    return result
