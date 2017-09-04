# distutils: language = c++

from __future__ import division
import sys

import numpy
import six

cimport cpython
cimport cython
from libcpp cimport vector
from cpython.sequence cimport *
from cpython.mapping cimport *
from cpython.iterator cimport *
from cpython.type cimport *
from cpython.number cimport *
from cpython.int cimport *

from fastrlock cimport rlock
