#!/usr/bin/python3

import sys

if __name__ == "__main__":

    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

        for d in range(num_args):
            print("{}: {}".format(d + 1, sys.argv[d + 1]))
