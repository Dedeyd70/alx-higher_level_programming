#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for d in range(x):
        try:
            print("{}".format(my_list[d]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return (count)
