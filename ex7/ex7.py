#################################################################
# FILE : ex7.py
# WRITER : Michael Hasson , mikey641 , 322893892
# EXERCISE : intro2cs2 ex7 2020
# DESCRIPTION: Recursion coding
#################################################################
LEFT_DIGIT_INDEX=0
ZERO_COUNTER_INDEX=1
FLOODED="*"

def print_to_n(n):
    """
    This function prints the integers from 1 to n recursively.
    :param n:Number when the print ends
    :return:None
    """
    if n<1:
        return None
    print_to_n(n-1)
    print(n)

def digit_sum(n):
    """
    This fucntion sums the digits of a number
    :param n: the number to sum it's digits
    :return: digit sum
    """
    return r_digit_sum(n)

def r_digit_sum(n,sum=0):
    """
    This is a subfunction of digit_sum, using recursion
    :param sum: 0 by default. This is a sum counter.
    :param n: the number to sum it's digits
    :return: digit sum
    """
    if n==0:
        return sum
    sum+=left_digit(n)[LEFT_DIGIT_INDEX]#adding left digit to the sum
    n-=left_digit(n)[LEFT_DIGIT_INDEX]*10**left_digit(n)[ZERO_COUNTER_INDEX] #removing the left digit
    return r_digit_sum(n,sum)
def left_digit(n,i=0):
    """
    This function returns the left digit of a number using recursion.
    :param n: The number to find it's left digit
    :param i: number of zeros counter. It means we have already divided the original number by 10^i=
    :return: tuple of the left digit, and i (how many 10^i we divided the original number)
    """
    if n<10:
        return int(n), i
    return left_digit(n/10,i+1)

def is_prime(n):
    """
    This function recieves a number and checks if it is prime recursively.
    :param n: The number to check
    :return: True if prime, False if not prime.
    """
    if n <=1:
        return False
    return not has_divisor_smaller_than(n,n)
def has_divisor_smaller_than(n,i):
    """
    This function recieves a number and checks if it has a divisor smaller than i recursively.
    :param n: The number to test
    :param i: Number from which we will check if "n" is divided by any smaller numbers
    :return: True if it has a divisor, False if not.
    """
    i-=1
    if i==1:
        return False
    if n//i == n/i:
        return True
    return has_divisor_smaller_than(n,i)
def play_hanoi (hanoi,n,src,dst,temp):
    """
    This game is used in hanoi_game.py as a solver for an hanoi puzzle.
    :param hanoi: object of the graphics of hanoi_game.py
    :param n:Number of disks the function needs to move from one pole to the other
    :param src:complex object representing the pole from which we want to move the disks
    :param dst:complex object representing the pole to which we want to move the disks
    :param temp:complex object representing the third pole
    """
    if n <= 0:
        return
    elif n==1:
        hanoi.move(src, dst)
        return
    elif n==2:
        hanoi.move(src, temp)
        hanoi.move(src, dst)
        hanoi.move(temp, dst)
    else:
        play_hanoi(hanoi, n-1,src,temp,dst)
        hanoi.move(src, dst)
        play_hanoi(hanoi,n-1,temp, dst, src)

def print_sequences (char_list,n):
    """
    This function prints a list of strings with "n" characters using the chars in char_list. It is allowed to use the
    same character more than once in a string.
    :param char_list: list of characters to use in the strings
    :param n: length of strings
    """
    for i in r_sequences(char_list,n,True):
        print (i)

def print_no_repetition_sequences (char_list,n):
    """
    This function prints a list of strings with "n" characters using the chars in char_list. It is not allowed to use
    the same character more than once in a string.
    :param char_list: list of characters to use in the strings
    :param n: length of strings
    """
    for i in r_sequences(char_list,n,False):
        print (i)

def r_sequences(char_list, n,repetition,new_char_lst=[]):
    """
    This function returns a list of strings with "n" characters using the chars in char_list.
    It does that recursively using the list of r_sequences of n-1, and altering it to match n.
    :param char_list: list of characters to use in the strings
    :param n: length of strings
    :param repetition: True if it is allowed to repeat a character in a string, else False.
    :param new_char_lst: empty list by default, usually inserted the r_sequences of n-1.
    :return: list of strings
    """
    if n==0:
        return [""]
    elif n==1:
        return char_list
    if new_char_lst == []:
        new_char_lst = char_list
    if n == 2:
        new_lst = []
        for i in char_list:
            for j in new_char_lst:
                if i not in j or repetition:
                    new_lst.append(i + j)
        return new_lst
    return r_sequences(char_list, 2, repetition,r_sequences(char_list, n - 1,repetition))

def parentheses(n):
    """
    This function returns a list of strings when each string contains n parentheses.
    :param n:Number of parentheses
    :return:list of strings of parentheses
    """
    if n==0:
        return [""]
    if n==1:
        lst=["()"]
        return lst
    lst=[]
    for i in parentheses(n-1):
        if i + "()" not in lst:
            lst.append(i + "()")
        if "()" + i not in lst:
            lst.append("()" + i)
        if "(" +i+ ")" not in lst:
            lst.append("(" +i+ ")")
        if ")(" in i and i.replace(")(",")()(",1) not in lst:
            lst.append(i.replace(")(",")()(",1))
        if "()" in i and i.replace("()","(())",1) not in lst:
            lst.append(i.replace("()","(())",1))
    return lst

def flood_fill (image,start):
    """
    This function recieves an image indicating flooded and dry places, and a start point for a flood, and alters the
    image by flooding indexes near the start and its' trail.
    :param image: image indicating flooded and dry places
    :param start: start point for a flood
    """
    row,column=start
    if row <= 0 or row>=len(image) or column<=0 or column >= len(image[row]):
        return
    if image[row][column]== "*":
        return
    flood_index(image,start)
    flood_fill(image,(row+1,column))
    flood_fill(image,(row-1,column))
    flood_fill(image,(row,column+1))
    flood_fill(image,(row,column-1))

def flood_index (image,index):
    """
    This function recieves an image and index and marks the recieved index as flooded
    :param image: image indicating flooded and dry places
    :param index: index to mark as flooded
    :return:
    """
    i,j=index
    image[i][j]=FLOODED