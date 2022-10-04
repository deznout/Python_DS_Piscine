#!/usr/bin/env python3

import timeit


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


if __name__ == '__main__':
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
              'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
              'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
              'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
              'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']

    # print(f'map = {using_map(emails)}')
    # print(f'loop = {using_loop(emails)}')
    # print(f'lst_comprhsn = {using_lst_comprhsn(emails)}')

    loop_time = timeit.timeit(f'{using_loop(emails)}', number=90000000)
    lst_comprhsn_time = timeit.timeit(f'{using_lst_comprhsn(emails)}', number=90000000)
    map_time = timeit.timeit(f'{using_map(emails)}', number=90000000)
    min_time = min(lst_comprhsn_time, loop_time, map_time)
    if min_time == lst_comprhsn_time:
        print("it is better to use a list comprehension")
    elif min_time == loop_time:
        print("it is better to use a loop")
    else:
        print("it is better to use a map")
    lst = sorted([lst_comprhsn_time, loop_time, map_time])
    for i in lst[:-1]:
        print(i, 'vs', end=' ')
    print(lst[-1])
