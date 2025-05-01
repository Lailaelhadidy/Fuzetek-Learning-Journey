import math

class Rectangle:
    def __init__(self, length, width):
        self.__length= length
        self.__width= width
    def calculate_area(self):
        return self.__length * self.__width
    def calculate_perimeter(self):
        return (2*self.__width) + (2*self.__length)
        #return 2* (self.__length * self.__width)
    def is_square(self):
        return self.__length == self.__width

    def scale_rectangle(self, scale_factor):
        return  Rectangle(scale_factor * self.__length, scale_factor * self.__width)

    def __add__(self, other):
        return Rectangle(self.__length + other.__length, self.__width + other.__width)


    def __sub__(self, other):
        return Rectangle(abs(self.__length - other.__length), abs(self.__width - other.__width))

    def __eg__(self, other):
        return self.__length == other.__length and self.__width == other.__width

    def __ne__(self, other):
        return not(self.__length == other.__length and self.__width == other.__width)
    #will give true if they are not equal

    def __str__(self):
        return f"the width equal {self.__width} \n  the length equal {self.__width}"