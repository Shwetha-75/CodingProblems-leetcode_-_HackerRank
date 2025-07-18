'''

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
 
 
'''

class Solution:
      def search(self, nums: list[int], target: int) -> bool:
          left,right=0,len(nums)-1
          while left<=right:
                mid=(left+right)//2 
                if nums[mid]==target:
                    return True 
                # if left , mid & right index values are same we don't know where we have to go so
                if nums[left]==nums[right]==nums[mid]:
                    left+=1
                    right-=1
                    continue 
                # check if left is sorted 
                
                if nums[left]<=nums[mid]:
                    if nums[left]<=target and target<nums[mid]:
                        
                        right=mid-1
                    else:
                        left=mid+1 
                else:
                    if nums[mid]<target and target<=nums[right]:
                        left=mid+1 
                    else:
                        right=mid-1
          return False
class TestApp:
      def testing_case_one(self):
          assert Solution().search([2,5,6,0,0,1,2],0)==True 
      def testing_case_two(self):
          assert Solution().search([2,5,6,0,0,1,2],3)==False
      def testing_case_three(self):
          assert Solution().search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1],2)==True 
      def testing_case_four(self):
          assert Solution().search([1,0,1,1,1,1],0)==True 
    