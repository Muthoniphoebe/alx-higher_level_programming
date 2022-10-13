#!/usr/bin/python3
class Square:
    """defines a square by:
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0)
    """
    def __init__(self, size=0):
        """Intialization
        """
        self.__size = size
    
    @property
    def size(self):
        """retrives square size."""
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns square value """
        return (self.__size * self.__size)
