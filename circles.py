from math import pi
import os
import sys
sys.path.append('C:/full/path')


def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number")

    if r < 0:
        raise ValueError("The radius can not be negative")

    return pi * (r ** 2)


#print(circle_area(2))
#print(os.getcwd()) # Get current working directory
print(os.path.realpath(__file__))
print(sys.path)
