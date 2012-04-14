#!/bin/sh

BENCH='p.primes(1000)'
REP=10

echo "THIS IS NOT A BENCHMARK"
echo "FUNCTION INTERFACE"

echo -n " python prime:\n\t"
python -m timeit -n $REP -s 'import prime as p' $BENCH

echo -n " hand coded python c-module:\n\t"
python -m timeit -n $REP -s 'import pyprime as p' $BENCH

echo -n " reimplementation of function in cython:\n\t"
python -m timeit -n $REP -s 'import pyxprime as p' $BENCH

echo -n " cython calling c func, return numpy array:\n\t"
python -m timeit -n $REP -s 'import pyxnpprime as p' $BENCH

echo -n " ctypes calling c func, return numpy array:\n\t"
python -m timeit -n $REP -s 'import ctnplibprime as p' $BENCH
