import os.path
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("pyxlibprime", ["modlibprime.pyx"],libraries=['prime'],library_dirs=[os.path.abspath('.')])]

setup(
  name = 'Cython test',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
