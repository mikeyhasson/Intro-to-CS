#################################################################
# FILE : quadratic_equation.py
# WRITER : Michael Hasson , mikey641 , 322893892
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A simple program that solves quadratic_equations
#################################################################
def quadratic_equation (a,b,c):
    """this function has 3 parameters a,b,c. based on the quadratic equation structure ax^2+bx+c=0
    it uses the quadratic formula to solve the equation. the solutions are returned in a tuple"""
    if (b**2-4*a*c) < 0: #if this expression is smaller than 0, the equation has no solution.
        return (None,None)
    solution1= (-b+ (b**2-4*a*c)**0.5)/(2*a)
    solution2= (-b- (b**2-4*a*c)**0.5)/(2*a)
    if solution1==solution2: #if the equation only has 1 solution, we return a tuple of (solution,None)
        solution2 = None
    return (solution1,solution2)

def quadratic_equation_user_input():
    """this function is the user interface of the program. it uses input to allow users to type in a,b,c and prints
    the solutions using the "quadratic_equation" function"""
    a,b,c=input ("Insert coefficients a, b, and c: ").split()
    a,b,c=float (a),float (b),float (c) #casting since numbers were str
    if a==0: #if a is 0, it is not a quadratic equation.
        print ("The parameter 'a' may not equal 0")
    else:
        solution1 = quadratic_equation(a,b,c)[0]
        solution2 = quadratic_equation(a,b,c)[1]
        if (solution2 == None):
            if (solution1 == None):
                print ("The equation has no solutions") #if both solutions are set has None, there is no solution
            else:
                print("The equation has 1 solution: " + str(solution1)) #if only the second solution is None, 1 solution
        else:
            print("The equation has 2 solutions: " + str(solution1) + " and " + str(solution2))