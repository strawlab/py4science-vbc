all: testlibfib libfib.so pyxlibfib.so fib.pyx

libfib.so: libfib.o
	$(CC) -Wall -g -fPIC -shared -o $@ $< -lc

testlibfib: libfib_main.c libfib.o
	$(CC) -Wall -g -o $@ $?

pyxlibfib.so: libfib.so modlibfib.pyx
	python pyxlibfibsetup.py build_ext --inplace

fib.pyx: fib.py
	cp -f $? $@

clean:
	rm -f testlibfib libfib.o libfib.so *.pyc
	rm -f pyxlibfib.so modlibfib.c
	rm -f fib.pyx
	rm -rf build
