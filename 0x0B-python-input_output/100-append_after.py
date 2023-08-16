#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """Appending a string after finding a keyword"""
    my_str = ""
    with open(filename, encoding="utf8") as fd:
        for row in fd:
            my_str += row
            if search_string in row:
                my_str += new_string

    with open(filename, mode="w") as fd:
        fd.write(my_str)
