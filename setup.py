#!/usr/bin/env python

import os
import sys

from distutils.command.sdist import sdist
from distutils.command.build_ext import build_ext
from setuptools import setup, Extension

setup_requires = ['fastrlock>=0.3']
install_requires = ['fastrlock>=0.3']

pyx_ext_modules = [Extension('segv._segv',
                         sources=['segv/_segv.pyx'],
                         libraries=[],
                         include_dirs=[],
                         define_macros=[])]
ext_modules = [Extension('segv._segv',
                         sources=['segv/_segv.cpp'],
                         libraries=[],
                         include_dirs=[],
                         define_macros=[])]

class BuildExt(build_ext):
    def run(self):
        import Cython
        import Cython.Build
        Cython.Build.cythonize(pyx_ext_modules, verbose=True)
        build_ext.run(self)

class Sdist(sdist):
    def __init__(self, *args, **kwargs):
        import Cython
        import Cython.Build
        Cython.Build.cythonize(pyx_ext_modules, verbose=True)
        sdist.__init__(self, *args, **kwargs)

setup(
    name='segv',
    version='1.0.0',
    url='https://github.com/sonots/cython-segv',
    author='sonots',
    author_email='sonots@gmail.com',
    packages=['segv'],
    zip_safe=False,
    setup_requires=setup_requires,
    install_requires=install_requires,
    ext_modules=ext_modules,
    cmdclass={'build_ext': BuildExt, 'sdist': Sdist},
)
