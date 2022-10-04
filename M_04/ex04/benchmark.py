#!/usr/bin/env python3


import timeit
import random
from collections import Counter


def loop_sum(num):
    res = 0
    for j in range(1, num + 1):
        res += j ** 2
    return res


def create_dict(nums):
    res = {}
    for i in nums:
        if i in res.keys():
            res[i] += 1
        else:
            res[i] = 1
    return res


def top_ten_dict(nums):
    dc = create_dict(nums)
    return sorted(dc.items(), key=lambda item: -item[1])[:10]


if __name__ == '__main__':
    num_lst = [random.randint(0, 100) for i in range(1000)]
    print('my function: ', timeit.timeit(f'create_dict({num_lst})', setup='from __main__ import create_dict', number=1))
    print('Counter: ', timeit.timeit(f'Counter({num_lst})', setup='from __main__ import Counter', number=1))
    print('my top: ', timeit.timeit(f'top_ten_dict({num_lst})', setup='from __main__ import top_ten_dict', number=1))
    print('Counter\'s top: ', timeit.timeit(f'Counter({num_lst}).most_common(10)',
                                            setup='from __main__ import Counter', number=1))
