'''
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.

'''

def singleNumber(nums):
    #Incomplete need to work for understanding
    a = b = 0
    for num in nums:    
        a, b = (~a & b & num) | (a & ~b & ~num),(~a & ~b & num) | (~a & b & ~num)
        print(~a,a,b,~b,num,~num)
    return b
    '''
    #Approach 1
    #Brute Force approach
    for i in nums:
        if nums.count(i)==1:
            return i '''
nums=[2,2,2,3]
print(singleNumber(nums))
print(~-1)