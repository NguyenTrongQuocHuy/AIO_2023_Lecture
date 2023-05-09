import math

def factorial_dev_(x):
    'This function is using to calculate the Factorial !'
    factorial_result_ = 1
    for i in range(1,x+1,1):
        factorial_result_ = factorial_result_*i
    return factorial_result_

def sin_x_estimation(x,n):
    'This function is using to estimate the sin(x)'
    result_ = 0
    for i in range(n+1):
        #result_ = result_ + (((-1)**i)*(((math.radians(x))**(2*i+1))/(factorial_dev_(2*i+1))))
        result_ = result_ + ((-1)**i)*(((x)**(2*i+1))/(factorial_dev_(2*i+1)))
    return result_

def cos_x_estimation(x,n):
    'This function is using to estimate the cos(x)'
    result_ = 0
    for i in range(n+1):
        result_ = result_ + (((-1)**i)*((x**(2*i))/(factorial_dev_(2*i))))
    return result_

def sin_h_x_estimation(x,n):
    'This function is using to estimate the sinh(x)'
    result_ = 0
    for i in range(n):
        result_ = result_ + (((x)**(2*i+1))/(factorial_dev_(2*i+1)))
    return result_

def cos_h_x_estimation(x,n):
    'This function is using to estimate the cosh(x)'
    result_ = 0
    for i in range(n):
        result_ = result_ + (((x)**(2*i))/(factorial_dev_(2*i)))
    return result_



print('Input the number you want to calculate')
number_ = input()

print('Input the level you want to calculte')
level_ = input()


try:
    number_ = float(number_)
    level_ = int(level_)
    if level_>=0:
        print('Sin(',number_,') =',sin_x_estimation(number_,level_))
        print('Cos(',number_,') =',cos_x_estimation(number_,level_))
        print('Sinh(',number_,') =',sin_h_x_estimation(number_,level_))
        print('Cosh(',number_,') =',cos_h_x_estimation(number_,level_))
    else:
        print('The level must be greater or equal to ZERO') 
except:
    print('Syntax error: \n Type of number must be float or interger\n Type of level must be interger')

    