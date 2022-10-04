#!/usr/bin/env python3


import timeit
import sys


def using_loop(mails):
    res = []
    for j in mails:
        if j[-10:] == "@gmail.com":
            res.append(j)
    return res


def using_lst_comprhsn(mails):
    res = [k for k in mails if k[-10:] == "@gmail.com"]
    return res


def using_map(mails):
    res = list(map(lambda j: j if j[-10:] == "@gmail.com" else None, mails))
    return res


def using_filter(mails):
    res = list(filter(lambda j: j[-10:] == "@gmail.com", mails))
    return res


if __name__ == '__main__':
    if len(sys.argv) == 3:
        emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                  'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                  'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                  'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                  'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
        if sys.argv[1] == "loop":
            print(timeit.timeit(f'{using_loop(emails)}', number=int(sys.argv[2])))
        elif sys.argv[1] == "list_comprehension":
            print(timeit.timeit(f'{using_lst_comprhsn(emails)}', number=int(sys.argv[2])))
        elif sys.argv[1] == "map":
            print(timeit.timeit(f'{using_map(emails)}', number=int(sys.argv[2])))
        elif sys.argv[1] == "filter":
            print(timeit.timeit(f'{using_filter(emails)}', number=int(sys.argv[2])))
