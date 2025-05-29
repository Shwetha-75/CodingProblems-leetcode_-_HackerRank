#In this problem 
#We have to find the duplicate element return the duplicate element
'''
def duplicate(array):
    for i in array:
        if array.count(i)>=2:
            return i
array=[1,2,2,3,4,5,6]
print(duplicate(array))
#Time limit exceded!!!

'''

from collections import Counter

def duplicate(array):
    return max(Counter(array),key=Counter(array).get)
   
array=[1,2,3,4,5,6,6,7]
print(duplicate(array))