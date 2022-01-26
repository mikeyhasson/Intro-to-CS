#################################################################
# FILE : largest_and_smallest.py
# WRITER : Michael Hasson , mikey641 , 322893892
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A simple program that finds the maximum and the minimum within 3 numbers
# I chose to check the returned value of these 3 numbers becuase:
# 13,13,13: to see how the function deals with 3 identical numbers
# 5,5.76,9.73: to see how the function deals with a mix of float and integer
#################################################################
def largest_and_smallest (num1,num2,num3):
    """this function returns the value of the maximum and minimum within 3 number as a tuple (max,min)"""
    max=num1
    if num2 > max:
        max=num2
    if num3 > max:
        max=num3
    min=num1
    if num2 < min:
        min=num2
    if num3 < min:
        min=num3
    return (max,min)

def check_largest_and_smallest():
    """this function checks if "largest_and_smallest" returns the expected values. if every case is as expected
    the function will return True, else, it will return False"""
    is_correct = True
    if largest_and_smallest(17,1,6) != (17,1):
        is_correct = False
    if largest_and_smallest(1,17,6) != (17,1):
        is_correct = False
    if largest_and_smallest(1,1,2) != (2,1):
        is_correct = False
    if largest_and_smallest(13,13,13) != (13,13):
        is_correct = False
    if largest_and_smallest(5,5.76,9.73) != (9.73,5):
        is_correct = False
    return is_correct