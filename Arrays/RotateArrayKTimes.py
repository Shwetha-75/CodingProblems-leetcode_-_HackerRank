'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

'''

class Solution:
      def rotateArray(self,nums:list[int],k:int):
          def helper(left:int,right:int):
              while left<=right:
                    nums[left],nums[right]=nums[right],nums[left]
                    left+=1
                    right-=1
          n=len(nums)
          k%=n
          helper(0,n-1)
          helper(0,k-1)
          helper(k,n-1)
class TestApp:
      def testing_case_one(self):
          nums=[1,2,3,4,5]
          Solution().rotateArray(nums,3)
          assert nums==[3,4,5,1,2]
      def testing_case_two(self):
          nums=[1,2,3,4,5,6,7]
          Solution().rotateArray(nums,3)
          assert nums==[5,6,7,1,2,3,4]
      def testing_case_three(self):
          nums=[1,2,3]
          Solution().rotateArray(nums,4)
          assert nums==[3,1,2]
          