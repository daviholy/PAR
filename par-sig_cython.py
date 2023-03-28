import par_sig as sig
import numpy as np
import timeit

y = np.random.uniform(size=100_000_000)
result = np.empty(y.shape[0] - 2,dtype=np.float64)
print(timeit.timeit( lambda: sig.smooth_signal(y,result), number = 10))

# print(result)
# sig.fast_smooth_signal(y,result)
print(timeit.timeit( lambda: sig.fast_smooth_signal(y,result), number = 10))
# print(result)
# sig.superfast_smooth_signal(y,result)
print(timeit.timeit( lambda: sig.superfast_smooth_signal(y,result), number = 10))
# print(result)