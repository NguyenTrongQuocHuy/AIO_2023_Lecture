import math
import numpy as np

def pascal_triangle_factor(n,k):
    'this function to calculate the factor at pos.#k of row#n of Pascal Triangle'
    result = (math.factorial(n))/((math.factorial(k))*math.factorial(n-k))
    return int(result)

def pascal_triangle_row(row):
    'this function to assembly all factor into row as list'
    lst_row = []
    i = 0
    for i in range(row+1):
        lst_row.append(pascal_triangle_factor(row,i))
    return lst_row

def fibonacci_sequence_(_length_):
    'This function is using for print the Fibonacci Sequence'
    if _length_ == 1:
        lst_factor_ = [0]
    elif _length_ >=2:
        lst_factor_ = [0,1]
        for i in range(2,_length_,1):
            factor_ = lst_factor_[i-2]+lst_factor_[i-1]
            lst_factor_.append(factor_)
    else:
        print('The length must be greater than ZERO')
    return lst_factor_

def print_pascal_triangle_(_level_):
    for r_o_w in range(_level_+1):
        print(np.array(pascal_triangle_row(r_o_w)))
    return 'Below is your required Pascal Triangle'
        

print('Input the level of pascal triangle')
level_ = input()

print('Input the length of Fibonnaci Sequence')
length_ = input()

try:
    level_ = int(level_)
    length_ = int(length_)
    if level_ < 0 :
        print('The level of Pascal Triangle must be equal or greater than ZERO')
    else:
        print('The result of Pascal Triangle is:\n',print_pascal_triangle_(level_))
    
    if length_ < 0:
        print('The length of Fibonacci Sequence must be equal or greater than ZERO')
    else:
        print('The result of Fibonacci Sequence is:\n',fibonacci_sequence_(length_))
except:
    print('Syntax Error: Type of level and length must be interger')
    