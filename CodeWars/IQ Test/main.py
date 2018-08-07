#!/usr/bin/python
# -*- encoding: utf-8 -*-

def iq_test(numbers):
    #your code here
    n_list = [int(n) for n in numbers.split(' ')]

    even = filter(lambda n: n % 2 == 0, n_list)
    odd = [n for n in n_list if n not in even]

    if len(even) == 1:
        position = n_list.index(even[0]) + 1
    elif len(odd) == 1:
        position = n_list.index(odd[0]) + 1

    return position

print iq_test("2 4 7 8 10")
