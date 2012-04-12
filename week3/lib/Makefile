all: testlibprime libprime.so pyxlibprime.so pyxprime.so

libprime.so: prime.o libprime.o
	$(CC) -Wall -g -fPIC -shared -o $@ $? -lc

testlibprime: libprime_main.c libprime.so
	$(CC) -Wall -g -o $@ $?

pyxlibprime.so: libprime.so modlibprime.pyx
	python pyxlibprimesetup.py build_ext --inplace

pyxprime.so: pyxprime.pyx
	python pyxprimesetup.py build_ext --inplace

clean:
	rm -f testlibprime libprime.o libprime.so *.pyc *.o
	rm -f pyxlibprime.so modlibprime.c
	rm -f prime.pyx
	rm -rf build
