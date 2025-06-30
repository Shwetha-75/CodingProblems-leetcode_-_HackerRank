class Solution:
      def countPartitions(self, nums: list[int]) -> int:
          total=0
          for num in nums:
              total+=num 
          n,left,count=len(nums),0,0
          for i in range(n-1):
              left+=nums[i]
              total-=nums[i]
              if not abs(left-total)%2:
                  count+=1
          return count 
class TestApp:
      def testing_case_one(self):
          assert Solution().countPartitions([10,10,3,7,6])==4
      def testing_case_two(self):
          assert Solution().countPartitions([1,2,2])==0
      def testing_case_thee(self):
          assert Solution().countPartitions([2,4,6,8])==3