#!/usr/bin/python3
"""
Resolving the NQUEEN Problem
"""


def check(queen, column):
    """
    function that checks if the position of each queen is valid
    """

    for d in range(column):
        if queen[d] == queen[column]:
            return False
        if abs(queen[d] - queen[column]) == abs(d - column):
            return False
    return True


def fulling(queen, column):
    """
    Recursive Function that change the queen when we
    get the correct position with no problems
    """

    tam = len(queen)
    ex = 0

    if column == tam:
        result = []

        for d in range(len(queen)):
            result.append([d, queen[d]])

        print(result)
        return True

    queen[column] = -1

    while(queen[column] < tam - 1 or ex == 1):
        queen[column] = queen[column] + 1
        if check(queen, column) is True:
            if column != tam:
                fulling(queen, (column + 1))
            else:
                ex = 1
                break
    return True


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    queen = []
    tam = int(sys.argv[1])
    for d in range(tam):
        queen.append(-1)

    fulling(queen, 0)
