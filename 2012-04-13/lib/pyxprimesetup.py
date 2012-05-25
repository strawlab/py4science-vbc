from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
  name = 'Cython test',
  cmdclass = {'build_ext': build_ext},
  ext_modules = [Extension("pyxprime", ["pyxprime.pyx"])]
)
