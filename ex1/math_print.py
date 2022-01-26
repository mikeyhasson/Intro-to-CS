#################################################################
# FILE : math_print.py
# WRITER : Michael Hasson , mikey641 , 322893892
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: A simple program that prints mathematical values.
#################################################################

import math

def golden_ratio():
    """this function prints the golden ratio"""
    print((1+5**0.5)/2)

def six_squared():
    """this function prints the value of six times two"""
    print(6**2)

def hypotenuse():
    """this function prints the hypotenuse of a triangle where the other lengths are 5 and 12"""
    print((5**2+12**2)**0.5) #Pythagorean equation

def pi():
    """this function prints the value of "pi" using module math"""
    print(math.pi)

def e():
    """this function prints the value of "e" using module math"""
    print(math.e)

def squares_area():
    """this function prints the area of squares with lengths from 1 to 10 as the length grows by 1 each print"""
    n=0
    while n<9:
         n=n+1
         print (n*n, end=" ")
    print (10*10)



if __name__ == "__main__" :
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()