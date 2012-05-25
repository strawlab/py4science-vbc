#!/bin/sh

REP=20
PRIMES=1000
BENCH="p.primes($PRIMES)"

echo "THIS IS NOT A BENCHMARK"
echo "FUNCTION API"

echo -n " python prime:\n\t"
python -m timeit -n $REP -s 'import prime as p' $BENCH

echo -n " hand coded python c-module:\n\t"
python -m timeit -n $REP -s 'import pyprime as p' $BENCH

echo -n " reimplementation of function in cython:\n\t"
python -m timeit -n $REP -s 'import pyxprime as p' $BENCH

echo "COMPARING CYTHON / NUMPY MEM MANAGEMENT STRATEGIES"
echo -n " c returns new array - np steals pointer via np-c API:\n\t"
python -m timeit -n $REP -s 'import pyxnpprime as p' "p.primes1($PRIMES)"

echo -n " prealloc in np, pass to c:\n\t"
python -m timeit -n $REP -s 'import pyxnpprime as p' "p.primes2($PRIMES)"

echo "COMPARING CTYPES / NUMPY MEM MANAGEMENT STRATEGIES"
echo -n " prealloc in np, pass to c:\n\t"
python -m timeit -n $REP -s 'import ctnpprime as p' "p.primes1($PRIMES)"
echo -n " c returns new array - np steals pointer via as_array:\n\t"
python -m timeit -n $REP -s 'import ctnpprime as p' "p.primes2($PRIMES)"
echo -n " c returns new array - np steals pointer via buffer interface:\n\t"
python -m timeit -n $REP -s 'import ctnpprime as p' "p.primes3($PRIMES)"

BENCH="primes.get_data()"
SETUP="primes=p.Prime($PRIMES); gc.enable()"
echo "CLASS API"

echo -n " cython class wrapper:\n\t"
python -m timeit -n $REP -s "import pyxlibprime as p; $SETUP" $BENCH

echo -n " ctypes class wrapper:\n\t"
python -m timeit -n $REP -s "import ctlibprime as p; $SETUP" $BENCH

echo -n " ctypes numpy class wrapper:\n\t"
python -m timeit -n $REP -s "import ctnplibprime as p; $SETUP" $BENCH

