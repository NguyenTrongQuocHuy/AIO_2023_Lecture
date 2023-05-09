import math
import random

def MAE_cal(n):
    i = 1
    cal = 0
    for i in range(n+1):
        cal = cal + abs(random.uniform(0,10)-random.uniform(0,10))
        print('Loss name: MAE, Sample',i,'predict',random.uniform(0,10),'target',random.uniform(0,10),'loss',cal)
    result = (1/n)*cal
    print('Final MAE:',result)
    return 'Done'

def MSE_cal(n):
    i = 1
    cal = 0
    for i in range(n):
        cal = cal + (random.uniform(0,10)-random.uniform(0,10))**2
        print('Loss name: MSE, Sample',i,'predict',random.uniform(0,10),'target',random.uniform(0,10),'loss',cal)
    result = (1/n)*cal
    print('Final MSE:', result)
    return 'Done'

def RMSE_cal(n):
    i = 1
    cal = 0
    for i in range(n):
        cal = cal + (random.uniform(0,10)-random.uniform(0,10))**2
        print('Loss name: RMSE, Sample',i,'predict',random.uniform(0,10),'target',random.uniform(0,10),'loss',cal)
    result = math.sqrt((1/n)*cal)
    print('Final RMSE:', result)
    return 'Done'


print('Input the number of sample')
num_samp = input()

try:
    num_samp = int(num_samp)
    print('Input the loss name (MAE|MSE|RMSE)')
    loss_name = input()
    if loss_name == 'MAE':
        print(MAE_cal(num_samp))
    elif loss_name == 'MSE':
        print(MSE_cal(num_samp))
    elif loss_name =='RMSE':
        print(RMSE_cal(num_samp))
    else:
        print('Loss name syntax is error!')
except:
    print('Number of sample must be interger number')