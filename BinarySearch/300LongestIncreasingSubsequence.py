'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 



'''

import bisect
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        result=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>result[-1]:
                result.append(nums[i])
            else:
                index=bisect.bisect_left(result,nums[i])
                result[index]=nums[i]
        return len(result)

class TestApp:
      def testing_case_one(self):
          assert Solution().lengthOfLIS([10,9,2,5,3,7,101,18])==4 
      def testing_case_two(self):
          assert Solution().lengthOfLIS([0,1,0,3,2,3])==4
      def testing_case_three(self):
          assert Solution().lengthOfLIS([7,7,7,7,7,7])==1