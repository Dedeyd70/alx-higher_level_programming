#!/usr/bin/python3

import sys

if __name__ == "__main__":

    arguments = sys.argv[1:]
    num_args = len(arguments)

    print("Number of argument(s):", num_args)

    if num_args == 0:
        print(".", end='\n')
    elif num_args == 1:
        print("Argument:", arguments[0])
    else:
        print("Arguments:")

        for d, arg in enumerate(arguments, 1):
            print("{}: {}".format(d, arg))
