'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.

'''

# Linear Search
class Solution:
    def findMin(self, nums: list[int]) -> int:
        # linear search 
        n=len(nums)
        for i in range(n-1):
            if nums[i+1]<nums[i]:
                return nums[i+1]
        return nums[0] if nums else nums
# Binary Search  
class Solution:
    def findMin(self,nums:list[int])->int:
        left,right=0,len(nums)-1
        while left<=right:
              mid=(left+right)//2 
             
              if mid==0 or mid==len(nums)-1:
                  return nums[mid]
              if nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1]:
                  return nums[mid]
              if nums[mid]<nums[mid+1]:
                 right=mid-1
              else:
                  left=mid+1
Solution().findMin([3,4,5,1,2])        
class TestApp:
      def testing_case_one(self):
          assert Solution().findMin([3,4,5,1,2])==1
      def testing_case_two(self):
          assert Solution().findMin([4,5,6,7,8,9,0,1,2])==0
      def testing_case_three(self):
          assert Solution().findMin([11,13,15,17])==11