import math

def binary_step_function(x):
    if x<0:
        result = 0
    else:
        result = 1
    return result

def sigmoid_function(x):
    result = (1)/(1+(math.e**-x))
    return result

def elu_function(x):
    if x<0:
        result = 0.01*((math.e**x)-1)
    else:
        result = x
    return result

print('input the factor "x"')
factor_x = input()

try: 
    factor_x = float(factor_x)
    print('input the activation function name as syntax included [binary,sigmoid,elu]')
    act_func = input()
    if act_func == 'binary':
        print('Result of Binary Step Function is:\n',binary_step_function(factor_x))
    elif act_func == 'sigmoid':
        print('Result of Signmoid Function is:\n',sigmoid_function(factor_x))
    elif act_func == 'elu':
        print('Result of Elu Function is:\n',elu_function(factor_x))
    else:
        print('ten_function_user is not supported...')
except:
    print('factor x must be a number')