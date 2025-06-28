'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''

def singleNumber(nums):
    #Approach 1
    #Linear approach or Brute force approach
    for i in nums:
        if nums.count(i)==1: return i 
        
nums=[3,3,4,5,5,1,1]
print(singleNumber(nums))

#Approach 2
def singleNumber2(nums):
    #store 0th index element 
    ans=nums[0]
    #Iterate through array  elements from index 1
    for i in nums[1::]:
        #taking bitwise xor of elemnts and update ans variable
        
        ans^=i
    return ans 

nums=[2,2,1]

print(singleNumber2(nums))
 #     0 1 2
 #nums[2,2,1]         At i=1       At i=2
        # ans=2   -->  0010          0000
        #              0010          0001
        #           ^  0000          0001
        #  result-->ans=1
        #