from distutils.core import setup, Extension
 
setup (name = 'PackageName',
        version = '1.0',
        description = 'This is a demo package',
        ext_modules = [Extension('pyprime', sources = ['modprime.c', 'libprime.c'])])
