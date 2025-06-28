class Solution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        sum_total=0
        for i in nums:
            sum_total+=i 
        result=sum_total
        for edge in edges:
            total=sum_total
            total-=nums[edge[0]]
            total-=nums[edge[1]]
            total+=max(nums[edge[0]]^k,nums[edge[0]])
            total+=max(nums[edge[1]]^k,nums[edge[1]])  
            result=max(result,total)  
        return result
Solution().maximumValueSum([24,78,1,97,44],6,[[0,2],[1,2],[4,2],[3,4]])
class TestApp:
      def testing_case_one(self):
          assert Solution().maximumValueSum([1,2,1],3,[[0,1],[0,2]])==6 
      def testing_case_two(self):
          assert Solution().maximumValueSum([2,3],7,[[0,1]])==9 
      def testing_case_three(self):
          assert Solution().maximumValueSum([7,7,7,7,7,7],3,[[0,1],[0,2],[0,3],[0,4],[0,5]])==42