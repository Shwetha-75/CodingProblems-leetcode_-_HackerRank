'''
You are given an array of positive integers nums.

An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:

prod(arr) is the product of all elements of arr.
gcd(arr) is the GCD of all elements of arr.
lcm(arr) is the LCM of all elements of arr.
Return the length of the longest product equivalent subarray of nums.

 

Example 1:

Input: nums = [1,2,1,2,1,1,1]

Output: 5

Explanation: 

The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

Example 2:

Input: nums = [2,3,4,5,6]

Output: 3

Explanation: 

The longest product equivalent subarray is [3, 4, 5].

Example 3:

Input: nums = [1,2,3,1,4,5,1]

Output: 5

 

Constraints:

2 <= nums.length <= 100
1 <= nums[i] <= 10

'''

import math
class Solution:
    def maxLength(self, nums: list[int]) -> int:
        # lcm_value=self.lcm(nums)*self.gcd(nums)
        left,right,product,max_len=0,0,1,0
        while right<len(nums) and nums[left:right+1]:
              product*=nums[right]
              lcm=self.lcm(nums[left:right+1])
              gcd=self.gcd(nums[left:right+1])
              if product==lcm*gcd:
                 max_len=max(max_len,right-left+1)
              elif product>lcm*gcd:
                  while product!=lcm*gcd and nums[left:right+1]:
                        lcm=self.lcm(nums[left:right+1])
                        gcd=self.gcd(nums[left:right+1])
                        product//=nums[left]
                        left+=1
              right+=1
                
        return max_len 
    def gcd(self,nums:list[int]):
        # print(nums)
        value=nums[0]
        for i in range(1,len(nums)):
            value=math.gcd(value,nums[i])
        return value
    def lcm(self,nums:list[int]):
        # print(nums)
        value=nums[0]
        for i in range(1,len(nums)):
            value=math.lcm(value,nums[i])
        return value 
class TestApp:
      def testing_case_one(self):
          assert Solution().maxLength([1,2,1,2,1,1,1])==5 
      def testing_case_two(self):
          assert Solution().maxLength([2,3,4,5,6])==3
      def testing_case_three(self):
          assert Solution().maxLength([1,2,3,1,4,5,1])==5    

