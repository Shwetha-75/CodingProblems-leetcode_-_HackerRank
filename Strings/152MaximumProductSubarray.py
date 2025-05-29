# Wrong Approach 
class Solution:
      def maxProduct(self, nums: list[int]) -> int:
          product=1
          end=0 
          max_product=float('-inf')
          while end<len(nums):
                product*=nums[end]
                if nums[end]>product:
                   product=nums[end]
                max_product=max(max_product,product)
                end+=1
          return max_product 
      
class Solution:
      def maxProduct(self, nums: list[int]) -> int:
          product=1 
          max_product=float('-inf')
          for i in range(len(nums)):
              product=1 
              for j in range(i,len(nums)):
                  product*=nums[j]
                  max_product=max(max_product,product)
          return max_product
                     
class Solution:
      def maxProduct(self, nums: list[int]) -> int:
          curr_min=curr_max=1 
          ans=max(nums)
          for num in nums:
              product=curr_max*num
              curr_max=max(product,curr_min*num,num)
              curr_min=min(product,curr_min*num,num)
              ans=max(ans,curr_max)
          return ans    
          
class TestApp:
      def testing_case_one(self):
          assert Solution().maxProduct([2,3,-2,4])==6 
      def testing_case_two(self):
          assert Solution().maxProduct([-2,0,-1])==0 
      def testing_case_three(self):
          assert Solution().maxProduct([0,2])==2 
      def testing_case_four(self):
          assert Solution().maxProduct([2,3,0,12])==12
      def testing_case_five(self):
          assert Solution().maxProduct([2,-5,-2,-4,3])==24