#!/usr/bin/python3
"""

function that create a Rectangle from the width and the height variables

"""


class Rectangle:
    """Representing a rectangle.
    Args:
        @width: integer
        @height: integer

    Raises:
        TypeError:
                 * width must be an integer
                 * height must be an integer
        ValueError:
                 * width must be >= 0
                 * height must be >= 0

    Returns:
        area: width * height
        perimeter: (2 * height) + (2 * width)
        __str__ : print the rectangle
        __repr__: print a message
        """
    def __init__(self, width=0, height=0):
        """Initializing a rectangle."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return (self.__width)

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return (self.__height)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.height * self.width)

    def perimeter(self):
        """Return the perimiter of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return (0)
        return ((2 * self.height) + (2 * self.width))

    def __str__(self):
        """Return the printable representaion of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.width == 0 or self.height == 0:
            return ("")
        figure = []
        for i in range(self.height):
            for j in range(self.width):
                figure = figure + "#"
            if (i < self.height - 1):
                figure = figure + "\n"
        return (figure)

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        print("Bye rectangle...")
