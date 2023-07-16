#!/usr/bin/python3

def max_integer(my_list=[]):
    length = len(my_list)

    if length == 0:
        return (None)

    maxi = my_list[0]
    for d in range(1, length):
        if my_list[d] > maxi:
            maxi = my_list[d]

            return (maxi)
