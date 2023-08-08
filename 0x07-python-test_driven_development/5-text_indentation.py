#!/usr/bin/python3
"""

A function that prints 2 new lines after ".?:" characters

"""


def text_indentation(text):
    """ Printing 2 new lines after ".?:" characters

    Args:
        text: input string

    Returns:
        No return

    Raises:
        TypeError: If text is not a string


    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    j = text[:]

    for d in ".?:":
        list_text = j.split(d)
        j = ""
        for f in list_text:
            f = f.strip(" ")
            j = f + d if j is "" else j + "\n\n" + f + d

    print(j[:-3], end="")
