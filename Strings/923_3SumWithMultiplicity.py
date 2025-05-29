import math
class Solution:
    def threeSumMulti(self, nums: list[int], target: int) -> int:
        count=0 
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==target:
                        count+=1 
        return count % (math.pow(10,9)+1) 
from collections import defaultdict
# Dynamic programming 
class Solution:
    def threeSumMulti(self, nums: list[int], target: int) -> int:
        count,hash_map=0,defaultdict(int) 
        for i in range(len(nums)):
            for j in range(i-1):
                hash_map[nums[j]+nums[i-1]]+=1
            count+=hash_map[target-nums[i]]
        return count % (math.pow(10,9)+1) 
class TestApp:
      def testing_case_one(self):
          assert Solution().threeSumMulti([1,1,2,2,3,3,4,4,5,5],8)==20 
      def testing_case_two(self):
          assert Solution().threeSumMulti([1,1,2,2,2,2],5)==12
      def testing_case_three(self):
          assert Solution().threeSumMulti([2,1,3],6)==1