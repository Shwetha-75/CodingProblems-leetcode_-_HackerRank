'''
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

 

Example 1:

Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
Example 2:

Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.
Example 3:

Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000

'''

class Solution:
    def specialArray(self, nums: list[int]) -> int:
        for x in range(len(nums)+1):
            count=0
            for num in nums:
                if num>=x:
                    count+=1
            if count==x:
                return x 
        return -1 
class Solution:
      def specialArray(self, nums: list[int]) -> int:
          left,right=0,len(nums)
          while left<=right:
                x=(left+right)//2 
                count=0 
                for num in nums:
                    if num>=x:
                        count+=1
                if x==count:
                    return x 
                if x<count:
                    left=x+1
                else:
                    right=x-1
          return -1     
class TestApp:
      def testing_case_one(self):
          assert Solution().specialArray([3,5])==2 
      def testing_case_two(self):
          assert Solution().specialArray([0,0])==-1
      def testing_case_three(self):
          assert Solution().specialArray([0,4,3,0,4])==3