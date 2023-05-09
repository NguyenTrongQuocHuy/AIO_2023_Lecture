import math
import time

def number_unit(number_test_count):
    'This function using to count the level of number such as hundred/thousand/million/billion...etc'
    count = 0
    while number_test_count%10 >=1:
        count = count + 1
        number_test_count = int(number_test_count/10)
    return count

def reverse_number(number__):
    'This function using to take the factor then multiply with level, so it will return reversed number'
    reversed_number = 0
    count = number_unit(number_)
    while count>=0:
        factor = number__%10
        reversed_number = reversed_number + factor * (10**(count-1))
        number__ = int(number__/10)
        count = count-1
    return int(reversed_number)


print('input the number')
number_ = int(input())

start_time = time.process_time()
print(reverse_number(number_))
stop_time = time.process_time()
print('it takes',stop_time-start_time)
