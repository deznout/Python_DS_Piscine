#!/usr/bin/env python3

# ~/goinfre/ml-25m/ratings.csv


import sys
import resource


def open_file(path):
    with open(path) as file:
        return file.readlines()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            for line in open_file(sys.argv[1]):
                pass
        except Exception as ex:
            print(ex)
    else:
        print('Filename as argument is needed!')
    usage = resource.getrusage(resource.RUSAGE_SELF)
    print(f'Peak Memory Usage = {usage.ru_maxrss / 1024 ** 3:.3f} GB')
    print(f'User Mode Time + System Mode Time = {usage.ru_utime + usage.ru_stime:.2f}s')
