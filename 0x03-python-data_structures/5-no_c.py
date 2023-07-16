#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)

    d = 0

    nw_string = my_string[:]

    for j in range(length):
        if (my_string[j] == 'c' or my_string[j] == 'C'):
            nw_string = nw_string[:(j - d)] + my_string[(j + 1):]
            d += 1

    return (nw_string)
