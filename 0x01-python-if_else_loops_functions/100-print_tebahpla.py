#!/usr/bin/python3
for d in reversed(range(97, 123)):
    print("{:c}".format(d if (d % 2 == 0) else (d - 32)), end="")
