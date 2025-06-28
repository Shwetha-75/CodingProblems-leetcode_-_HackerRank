'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?

'''
class Solution:
      def movingZeroesToEnd(self,nums:list[int]):
          stack,count,index=[],0,0
          n=len(nums)
          for i in range(n):
              if nums[i]!=0:
                 stack.append(nums[i])
              else:
                  count+=1
          for i in range(n):
              if index<len(stack):
                  nums[i]=stack[index]
                  index+=1
              else:
                  nums[i]=0 
          return nums

class TestApp:
      def testing_case_one(self):
          assert Solution().movingZeroesToEnd([0,1,0,3,12])==[1,3,12,0,0]
      def testing_case_two(self):
          assert Solution().movingZeroesToEnd([4,5,0,7,0,3,2,0])==[4,5,7,3,2,0,0,0]