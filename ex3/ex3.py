#################################################################
# FILE : ex3.py
# WRITER : Michael Hasson , mikey641 , 322893892
# EXERCISE : intro2cs2 ex3 2020
# DESCRIPTION: Useful functions for lists and math.
#################################################################
def input_list():
    """this function creates a list based on user input. using input, the user inserts numbers until he inserts an
    empty string. The fucntion returns a list containing the numbers the user inserted, with the sum of them being
    the end of the list"""
    user_list = list()
    user_input= input()
    sum=0
    if user_input== "": #if the first user input is an empty string. a list containing only 0 will be returned
        return [0]
    while user_input != "":
        user_list.append(float(user_input))
        sum+=float(user_input)
        user_input=input()
    user_list.append(sum)
    return user_list

def inner_product(vec_1, vec_2):
    """this function calculates the inner product of 2 vectors"""
    if len(vec_1) != len(vec_2): #if the lists are not in same length, None is returned
        return None
    if len(vec_1) == 0: #if the lists are empty, return 0
        return 0
    inner_product_value=0
    for i in range(len(vec_1)):
        inner_product_value+= vec_1[i]*vec_2[i]
    return inner_product_value

def sequence_monotonicity(sequence):
    """this function checks the monotonicity of a sequence and returns a list with 4 boolean values
    0. monotonically increasing 1. strictly monotonically increasing 2.monotonically decreasing
    3. strictly monotonically decreasing"""
    if len (sequence) <=1:
        return [True]*4
    increase=strict_increase=decrease=strict_decrease=True
    for i in range(1,len(sequence)):
        if sequence[i-1] == sequence[i]: #if A(n-1)== A(n), the sequence is not strict
            strict_increase=strict_decrease =False
        if sequence[i-1] < sequence[i]: #if A(n-1)< A(n), the sequence is not decreasing
            decrease=strict_decrease = False
        if sequence[i-1] > sequence[i]: #if A(n-1) > A(n), the sequence is not increasing
            increase=strict_increase = False
    return [increase, strict_increase, decrease, strict_decrease]

def monotonicity_inverse(def_bool):
    """this function creates a sequence based on 4 boolean values about the monotonicity of it,
     mentioned in previous function"""
    increase, strict_increase, decrease, strict_decrease = def_bool
    if increase==strict_increase==decrease==strict_decrease==True:
        return None
    if strict_decrease and not decrease or strict_increase and not increase: #strict in/decrease is first a in/decrease
        return None
    if increase and decrease:
        return [2,2]
    if increase:
        return [1,2,3,4] if strict_increase else [1,2,2,4]
    if decrease:
        return [4,3,2,1] if strict_decrease else [4,2,2,1]
    return [1,3,1,3] #def_bool is all False

def primes_for_asafi(n):
    """this function returns a list of prime numbers. the list's length is determined by the parameter n"""
    if n==0:
        return []
    primes_list=[2] #first prime number is 2
    current_num=primes_list[0]
    while len(primes_list)<n:#loop runs until the prime numbers list's length is "n"
        current_num += 1
        for i in primes_list: #if the number is divided by one of the smaller primes, it is not prime.
            if current_num % i == 0:
                break
        else: #if the number was undividable by any smaller prime, it is prime
            primes_list.append(current_num)
    return primes_list

def sum_of_vectors(vec_lst):
    """this function sums a list of vectors into one vector (returned as a list)"""
    if vec_lst == []: #if vec_lst is empty, None will be returned
        return None
    if vec_lst[0] == []: #if the lists inside vec_lst are empty, an empty list will be returned
        return []
    sum_list=[0]*len(vec_lst[0]) #creating a list of zeros to which we will add the sum
    for i in range(len(vec_lst)):
        for j in range(len(vec_lst[i])):
            sum_list[j]+=vec_lst[i][j]
    return sum_list

def num_of_orthogonal(vectors):
    """this functions checks how many orthogonal vectors are there in a list of vectors."""
    number_of_orthogonals = 0
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            if inner_product(vectors[i],vectors[j])== 0 and i != j: # i != j to avoid self pairs
                number_of_orthogonals+=1
    return number_of_orthogonals/2 #since we went through each orthogonal twice

