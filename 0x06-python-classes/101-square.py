#!/usr/bin/python3
"""square"""


class Square:
    """Defines a square """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        """square function"""
        return (self.__size ** 2)

    @property
    def size(self):
        """square function"""
        return (self.__size)

    @property
    def position(self):
        """square function"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple)):
            raise TypeError('position must be a tuple of 2 positive integers')
        for i in range(len(value)):
            if value[i] < 0:
                raise TypeError('position must be a tuple of 2 positive integers')
            if not (isinstance(value[i], int)):
                raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        
    @size.setter
    def size(self, value):
        if not (isinstance(value, int)):
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def new_print(self):
        """print the square in position"""
        x = ''
        if self.size == 0:
            return ('\n')
        for i in range(self.position[1]):
            x += "\n"
        for k in range(self.size):
            for y in range(self.position[0]):
                x += ' '
            for q in range(self.size):
                x += "#"
            x += "\n"
        return x

    def my_print(self):
        """square function"""
        print(self.new_print(), end='')
