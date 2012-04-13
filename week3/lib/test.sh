#!/bin/bash

export LD_LIBRARY_PATH=`pwd`

echo testlibprime
time $(./testlibprime >/dev/null)

echo pyxlibprime
time $(python -c 'import pyxlibprime; pyxlibprime.Prime(2000)._print()' > /dev/null)

echo ctlibprime
time $(python -c 'import ctlibprime; ctlibprime.Prime(2000)._print()' > /dev/null)

echo pyxprime
time $(python -c 'import pyxprime; print pyxprime.primes(2000)' > /dev/null)

echo pyxnpprime
time $(python -c 'import pyxnpprime; print pyxnpprime.primes(2000)' > /dev/null)

echo pyprime
time $(python -c 'import pyprime; print pyprime.primes(2000)' > /dev/null)

echo prime
time $(python -c 'import prime; print prime.primes(2000)' > /dev/null)


