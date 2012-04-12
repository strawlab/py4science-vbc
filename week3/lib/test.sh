#!/bin/bash

echo testlibprime
time $(./testlibprime >/dev/null)

echo pyxlibprime
time $(python -c 'import pyxlibprime; pyxlibprime.Prime(2000)._print()' > /dev/null)

echo ctlibprime
time $(python -c 'import ctlibprime; ctlibprime.Prime(2000)._print()' > /dev/null)

echo pxyprime
time $(python -c 'import pyxprime; print pyxprime.primes(2000)' > /dev/null)

echo prime
time $(python -c 'import prime; print prime.primes(2000)' > /dev/null)

