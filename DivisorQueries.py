'''
Consider the following function:
F(X)=Number of divisiors of integer X
You are given an array that consists of N integers. 
You are also provided M queries. 
There acn be only one type of query, query(l,r). 
You are required to determine the  product of all the numbers in the ranfe from l to .
The output can contain the values of la nd r. Your task is to print the result of function  F(X) mod 10^9+7 for that product.
For the 1st query, the product is 2, F(2)=2. For the second query, product=720
 , F(720)=30
 
'''


from functools import *
import math

def findProduct(list1,range1,range2):
    #creating the sub list (sub array)
    tempList=list1[range1-1:range2:]
    #[1,2,3,4,5,6]--> list elements
    #1 2--> range1 range2
    #indexing should start from range1-1 to range2   0:2--->0,1
    #templist=[0:2]
    #product-->1*2=2
    product=reduce(lambda i,j:i*j,tempList)
    #to find the divisors
    return finMod(product)
def finMod(product):
    #counting the number of divisors 
    #2-->[1,2]-->len([1,2])-->2
    divisors=len([i for i in range(1,product+1) if product%i==0])
    return divisors

#first line suze of the list and number of queries
value=list(map(int,input().split()))
#list elements
list1=list(map(int,input().split()))
for i in range(value[1]):
    #range
    range=list(map(int,input().split()))
    print(findProduct(list1,range[0],range[1]))
    

    
    