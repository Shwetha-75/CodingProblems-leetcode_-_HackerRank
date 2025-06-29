'''
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

 

Example 1:

Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
step by step sum
startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2
Example 2:

Input: nums = [1,2]
Output: 1
Explanation: Minimum start value should be positive. 
Example 3:

Input: nums = [1,-2,-3]
Output: 5
 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100

'''

class Solution:
      def minStartValue(self, nums: list[int]) -> int:
          startValue=1
          while True:
                flag=True 
                prefix_sum=nums[0]+startValue 
                if prefix_sum<1:
                   startValue+=1
                   continue
                for i in range(1,len(nums)):
                    prefix_sum+=nums[i]
                    if prefix_sum<1:
                       flag=False 
                       break 
                if flag:
                   return startValue 
                startValue+=1

class TestApp:
      def testing_case_one(self):
          assert Solution().minStartValue([-3,2,-3,4,2])==5 
      def testing_case_two(self):
          assert Solution().minStartValue([1,2])==1
      def testing_case_three(self):
          assert Solution().minStartValue([1,-2,-3])==5
         
         