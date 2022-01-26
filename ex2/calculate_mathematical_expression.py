#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Michael Hasson , mikey641 , 322893892
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A simple program containing 2 functions which calculates mathematical expressions
#################################################################
def calculate_mathematical_expression (num1, num2, operation):
    """this function calculates a mathematical expression using 3 parameters: the first 2 are numbers,
    the third is the operation you would like to use on those numbers. operations can only be +,-,/,*"""
    if operation == "/" and num2==0: #if num2 is 0, we return the value "None" since we can't divide by zero
        return None
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/":
        return num1/num2
    return None

def calculate_from_string (math_expression):
    """this function calculates the value of an expression in the form of: number expression number"""
    num1,operation,num2=math_expression.split() #since the expression is divided by spacing, we use the split function
    num1,num2= float(num1), float(num2) #casting to float since the numbers were strings
    return calculate_mathematical_expression (num1,num2,operation)
