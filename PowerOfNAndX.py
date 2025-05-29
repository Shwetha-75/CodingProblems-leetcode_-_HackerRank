#Problem to find x^n
from decimal import Decimal

def powerOfNumber(x,n):
    '''#Approach 1
    if n==0: return 1
    if n<0:
        n*=-1
        return 1/Decimal((n*Decimal(x).ln()))
    return pow(x,n)'''
    #Approach 2
    return x**n
x=2.00000
n=-2147483648
print(powerOfNumber(x,n))