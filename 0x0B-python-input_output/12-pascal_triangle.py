#!/usr/bin/python3
"""Defining a Pascal's Triangle function."""


def pascal_triangle(n):
    """Displaying  Pascal's Triangle of size n

    Returns:
    list of nummber in triangle
    """
    if n < 1:
        return []

    tri_angle = [[1]]
    while len(tri_angle) != n:
        triangle = tri_angle[-1]
        tmp = [1]
        for number in range(len(triangle) - 1):
            tmp.append(triangle[number] + triangle[number + 1])
        tmp.append(1)
        tri_angle.append(tmp)
    return tri_angle
