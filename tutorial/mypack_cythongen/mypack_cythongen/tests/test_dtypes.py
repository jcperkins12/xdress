"""Tests the part of dtypes that is accessible from Python."""
###################
###  WARNING!!! ###
###################
# This file has been autogenerated
from __future__ import print_function

import nose
from nose.tools import assert_equal, assert_not_equal, assert_raises, raises, \
    assert_almost_equal, assert_true, assert_false, assert_in

from numpy.testing import assert_array_equal, assert_array_almost_equal

import os
import numpy  as np

from mypack_cythongen import dtypes


# dtypeStr
def test_dtype_str():
    a = np.array(['Aha', 'Take', 'Me', 'On'], dtype=dtypes.xd_str)
    #for x, y in zip(a, np.array(['Aha', 'Take', 'Me', 'On'], dtype=dtypes.xd_str)):
    #    assert_equal(x, y)
    a[:] = ['On', 'Me', 'Take', 'Aha']
    #for x, y in zip(a, np.array(['On', 'Me', 'Take', 'Aha'], dtype=dtypes.xd_str)):
    #    assert_equal(x, y)
    a = np.array(['Aha', 'Me', 'Aha', 'Me'] + ['Take', 'On', 'Take', 'On'], dtype=dtypes.xd_str)
    #for x, y in zip(a, np.array(['Aha', 'Me', 'Aha', 'Me'] + ['Take', 'On', 'Take', 'On'], dtype=dtypes.xd_str)):
    #    assert_equal(x, y)
    b =  np.array((['Aha', 'Me', 'Aha', 'Me'] + ['Take', 'On', 'Take', 'On'])[::2], dtype=dtypes.xd_str)
    #for x, y in zip(a[::2], b):
    #    assert_equal(x, y)
    a[:2] = b[-2:]
    print(a)



if __name__ == '__main__':
    nose.run()
