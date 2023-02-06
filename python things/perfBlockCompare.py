'''
Using timeit module to compare the performance of code blocks
Version 0.1 - 01/10/2022
Alex Anderson
'''
import timeit
import numpy as np

def time_range(size):
    for i in range(size):
        pass

def time_arange(size):
    np.arange(size)

if __name__ == '__main__':

    # for smaller arrays
    print('Array Size: 1000')

    start = timeit.default_timer()
    time_range(1000)
    range_time_1 = timeit.default_timer() - start

    start = timeit.default_timer()
    time_arange(1000)
    arange_time_1 = timeit.default_timer() - start

    # for large arrays
    print('Array Size: 1000000')

    start = timeit.default_timer()
    time_range(1000000)
    range_time_2 = timeit.default_timer() - start

    start = timeit.default_timer()
    time_arange(1000000)
    arange_time_2 = timeit.default_timer() - start

    print(f'size 1000: range() took {range_time_1}')
    print(f'size 1000: arange() took {arange_time_1}')
    print(f'size 1000000: range() took {range_time_2}')
    print(f'size 1000000: arange() took {arange_time_2}')