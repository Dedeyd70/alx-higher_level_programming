#!/usr/bin/python3
def magic_calculation(a, b):
    output = 0
    for d in range (1, 3):
        try:
            if d > a:
                raise Execption("Too Far")
            output += a ** b / d
        except Exeception:
            output = b + a
            break
    return (ourput)
