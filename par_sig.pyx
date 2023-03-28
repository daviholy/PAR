# distutils: language = c++

import numpy as np


cdef extern from "par-sig_cpp.cpp" :
    pass

cdef extern from "par-sig_cpp.h":
    void smooth_signal_cpp(const double * y, double * result, int result_size)
    void smooth_signal_cpp_vec(const double * y, double * result, int result_size)


def smooth_signal(double[::1] y, double[::1] result):
    assert y.shape[0] == result.shape[0] + 2
    cdef int i
    cdef int size = y.shape[0]
    for i in range(1,size - 1):
        result[i-1] = (y[i] + y[i-1] + y[i+1])/3.0

def der_signal(double[::1]y, double[::1] result):
    assert y.shape[0] == result.shape[0] + 1
    cdef int i
    cdef int size = y.shape[0]
    for i in range(1,size):
        result[i-1] = y[i] - y[i-1]
    
def fast_smooth_signal(double[::1] y, double[::1] result):
    assert y.shape[0] == result.shape[0] + 2
    cdef int size_result = result.shape[0]
    smooth_signal_cpp(&y[0], &result[0], size_result)

def superfast_smooth_signal(double[::1] y, double[::1] result):
    assert y.shape[0] == result.shape[0] + 2
    cdef int size_result = result.shape[0]
    smooth_signal_cpp_vec(&y[0], &result[0], size_result)