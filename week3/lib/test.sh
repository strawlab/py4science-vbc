#!/bin/bash

export LD_LIBRARY_PATH=`pwd`

echo -e "\ntestlibprime"
time $(./testlibprime >/dev/null)

echo -e "\npyxlibprime"
time $(python -c 'import pyxlibprime; pyxlibprime.Prime(2000)._print()' > /dev/null)

echo -e "\nctlibprime"
time $(python -c 'import ctlibprime; ctlibprime.Prime(2000)._print()' > /dev/null)

echo -e "\npyxprime"
time $(python -c 'import pyxprime; print pyxprime.primes(2000)' > /dev/null)

#echo -e "\npyxnpprime"
#time $(python -c 'import pyxnpprime; print pyxnpprime.primes(2000)' > /dev/null)

echo -e "\npyprime"
time $(python -c 'import pyprime; print pyprime.primes(2000)' > /dev/null)

echo -e "\nprime"
time $(python -c 'import prime; print prime.primes(2000)' > /dev/null)


