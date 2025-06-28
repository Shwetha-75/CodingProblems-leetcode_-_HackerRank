'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 
'''
#the above problem
#its like game
#initially my points will be zero 
#im going on the way 
#when i encounter any obstacle the my score will be reduced by 1
#and also if the obstacle point is greater than my points ill be grabing the points of obstacle 
#to my pints 
#but each everytime i entercounter obstacle whether i have more [points or not ] ill be 
#reducing my score by 1

def checkJump(nums):
    myjump=0
    for i in nums:
        if myjump<0:
            return myjump
        elif i>myjump:
            myjump=i
        myjump-=1
    return myjump-1
nums=[2,3,0,1,4] 
print(checkJump(nums))

