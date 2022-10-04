#!/usr/bin/env python3


import timeit
import sys
from functools import reduce


def loop_sum(num):
    res = 0
    for j in range(1, num + 1):
        res += j ** 2
    return res


def reduce_sum(num):
    res = reduce(lambda a, b: a + b ** 2, [int(x) for x in range(1, num + 1)])
    return res


if __name__ == '__main__':
    if len(sys.argv) == 4:
        if sys.argv[1] == "loop":
            # print(loop_sum(int(sys.argv[3])))
            print(timeit.timeit(f'{loop_sum(int(sys.argv[3]))}', number=int(sys.argv[2])))
        elif sys.argv[1] == "reduce":
            # print(reduce_sum(int(sys.argv[3])))
            print(timeit.timeit(f'{reduce_sum(int(sys.argv[3]))}', number=int(sys.argv[2])))
