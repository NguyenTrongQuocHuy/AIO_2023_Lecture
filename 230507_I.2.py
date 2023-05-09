import math

def precision_cal(x,y):
    pre = (x)/(x+y)
    return pre

def recall_cal(x,z):
    recall = (x)/(x+z)
    return recall

def F1_score(x,y,z):
    result = 2*((precision_cal(x,y)*recall_cal(x,z))/(precision_cal(x,y)+recall_cal(x,z)))
    return result

print('Input the factor Tp')
Tp = input()
print('Input the factor Fp')
Fp = input()
print('Input the factor Fn')
Fn = input()

try:
    Tp = int(Tp)
    Fp = int(Fp)
    Fn = int(Fn)
    if Tp>0 and Fp>0 and Fn>0:
        print('Precision is', precision_cal(Tp,Fp))
        print('Recall is', recall_cal(Tp,Fn))
        print('F1-score is', F1_score(Tp,Fp,Fn))
    else:
        print('Tp,Fp,Fn must be greater than zero')
except:
    print('Value error! Tp,Fp,Fn must be interger')

