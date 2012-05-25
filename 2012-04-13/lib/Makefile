all: testlibprime libprime.so pyxlibprime.so pyxprime.so pyprime.so pyxnpprime.so

libprime.so: libprime.c
	$(CC) -Wall -g -fPIC -shared -o $@ $? -lc

testlibprime: libprime_main.c libprime.so
	$(CC) -Wall -g -o $@ $?

pyxlibprime.so: libprime.so pyxlibprime.pyx
	python pyxlibprimesetup.py build_ext --inplace

pyxnpprime.so: libprime.so pyxnpprime.pyx
	python pyxnpprimesetup.py build_ext --inplace

pyxprime.so: pyxprime.pyx
	python pyxprimesetup.py build_ext --inplace

pyprime.so: modprime.c
	python modprimesetup.py build
	cp build/`python -c 'import distutils.util; print "lib."+distutils.util.get_platform()+"-2.7"'`/pyprime.so .

clean:
	rm -f testlibprime
	rm -f *.pyc *.o *.so
	rm -f pyxlibprime.c
	rm -f pyxprime.c
	rm -rf build
