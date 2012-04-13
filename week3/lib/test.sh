#!/bin/bash

export LD_LIBRARY_PATH=`pwd`

echo -e "\n python"
time $(python -c 'import prime; print prime.primes(2000)' > /dev/null)

echo -e "\n c"
time $(./testlibprime >/dev/null)

echo -e "\n pyxlibprime"
time $(python -c 'import pyxlibprime; pyxlibprime.Prime(2000)._print()' > /dev/null)

echo -e "\n ctlibprime"
time $(python -c 'import ctlibprime; ctlibprime.Prime(2000)._print()' > /dev/null)

echo -e "\n ctnplibprime"
time $(python -c 'import ctnplibprime; print ctnplibprime.calculate_primes(2000)' > /dev/null)

echo -e "\n pyxprime"
time $(python -c 'import pyxprime; print pyxprime.primes(2000)' > /dev/null)

echo -e "\n pyprime"
time $(python -c 'import pyprime; print pyprime.primes(2000)' > /dev/null)

#echo -e "\npyxnpprime"
#time $(python -c 'import pyxnpprime; print pyxnpprime.primes(2000)' > /dev/null)




