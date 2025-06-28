class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        count=start=end=0 
        product=1
        while end<len(nums):
              product*=nums[end]
              while start<=end and product>=k:
                    product//=nums[start]
                    start+=1 
              count+=end-start+1 
              end+=1
        return count 
class TestApp:
      def testing_case_one(self):
          assert Solution().numSubarrayProductLessThanK([10,5,2,6],100)==8 
      def testing_case_two(self):
          assert Solution().numSubarrayProductLessThanK([1,2,3],0)==0