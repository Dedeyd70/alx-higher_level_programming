#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    res = 0

    for d in range(x):
        try:
            print("{:d}".format(my_list[d]), end="")
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            res += 1
    print()
    return (res)
