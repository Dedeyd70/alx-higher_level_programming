#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except Exception:
            result = b + a
            break
<<<<<<< HEAD
    return result
=======
    return (output)
>>>>>>> 8b0c43e600c79b279d7f1d7b8c4ef613abb61bc4
