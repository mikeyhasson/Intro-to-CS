#################################################################
# FILE : shapes.py
# WRITER : Michael Hasson , mikey641 , 322893892
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A simple program that calculates the area of 3 shapes: circles, rectangles and equilateral triangles
#################################################################
import math
def circle_area(radius):
    """ths function calculates the area of a circle using its radius length"""
    return math.pi * radius ** 2


def rectangle_area(side1, side2):
    """ths function calculates the area of a rectangle using using the 2 sides' length"""
    return side1 * side2

def triangle_area(side):
    """this function calculates the area of equilateral triangle using its side's length"""
    return ((3 ** 0.5) * (side ** 2)) / 4

def shape_area():
    """this function is the user interface of the program"""
    shape=input('Choose shape (1=circle, 2=rectangle, 3=triangle): ')

    if shape=="1": #calculates circle's area
        radius= float(input ())
        return circle_area(radius)

    if shape=="2": #calculates rectangle's area
        rectangle_side1=float(input())
        rectangle_side2=float(input())
        return rectangle_area(rectangle_side1,rectangle_side2)

    if shape=="3": #calculates triangle's area
        triangle_side= float(input())
        return triangle_area(triangle_side)
    return None #if the chosen shape was not 1, 2 or 3, None will be returned