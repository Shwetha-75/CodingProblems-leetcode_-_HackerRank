'''
 Given an integer array nums and an integer k, return true 
 if there are two distinct indices i and j in the array 
 such that nums[i] == nums[j] and abs(i - j) <= k.


Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
'''

#My First Approach
'''
def duplicate(array,k):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]==array[j] and abs(i-j)<=k:
                return True
    return False

#array=[1,2,3,1]
#k=3-->True
array=[1,2,3,1,2,3]
k=2# False
print(duplicate(array,k))'''

#Second Approach using Hash Map

def duplicate(array,k):
    #creating hash map
    dict1={}
    for i,num in enumerate(array):
        #checking if the elment is in dict or not if it is there 
        #then getting the index from element and taking abs difference 
        #comparing with k
        if num in dict1 and abs(dict1[num]-i)<=k:
            return True
        else:
            #adding element-->key
            #adding index-->value
            dict1[num]=i
    return False
array=[1,2,3,1]
k=3
print(duplicate(array,k))