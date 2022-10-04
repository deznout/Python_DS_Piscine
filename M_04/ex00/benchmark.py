#!/usr/bin/env  python3

import timeit


def using_loop(mails):
    res = []
    for i in mails:
        if i[-10:] == "@gmail.com":
            res.append(i)
    return res


def using_lst_comprhsn(mails):
    res = [i for i in mails if i[-10:] == "@gmail.com"]
    return res


if __name__ == '__main__':
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
              'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
              'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
              'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
              'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    print(using_loop(emails))
    loop_time = timeit.timeit(f'{using_loop(emails)}', number=90000000)
    lst_comprhsn_time = timeit.timeit(f'{using_lst_comprhsn(emails)}', number=90000000)
    if lst_comprhsn_time <= loop_time:
        print("it is better to use a list comprehension")
        print(lst_comprhsn_time, "vs", loop_time)
    else:
        print("it is better to use a loop")
        print(loop_time, 'vs', lst_comprhsn_time)
