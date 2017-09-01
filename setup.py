#!/usr/bin/env python

import os
import sys

from distutils.command.sdist import sdist
from distutils.command.build_ext import build_ext
from setuptools import setup, Extension
import Cython.Compiler.Main as cython_compiler

setup_requires = ['fastrlock>=0.3']
install_requires = ['fastrlock>=0.3']

def cythonize(src):
    sys.stderr.write("cythonize: %r\n" % (src,))
    cython_compiler.compile([src], cplus=True)

class BuildExt(build_ext):
    def build_extension(self, ext):
        return build_ext.build_extension(self, ext)

class Sdist(sdist):
    def __init__(self, *args, **kwargs):
        cythonize('segv/_segv.pyx')
        sdist.__init__(self, *args, **kwargs)

ext_modules = [Extension('segv._segv',
                         sources=['segv/_segv.cpp'],
                         libraries=[''],
                         include_dirs=[''],
                         define_macros=[''])]

setup(
    name='segv',
    version='1.0.0',
    url='https://github.com/sonots/cython-segv',
    author='sonots',
    author_email='sonots@gmail.com',
    packages=['segv'],
    setup_requires=setup_requires,
    install_requires=install_requires,
    ext_modules=ext_modules,
    cmdclass={'build_ext': BuildExt, 'sdist': Sdist},
)
