#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return (None)
    print("\n".join([" ".join(["{:d}".format(nbr) for nbr in y]) for y in matrix]))
