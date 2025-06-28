class Solution:
        def countCompleteSubarrays(self, nums: list[int]) -> int:
            k=len(set(nums))
            count=0
            for i in range(len(nums)-k+1):
                for j in range(i+k,len(nums)+1):
                    
                    if len(set(nums[i:j:]))==k:
                        count+=1 
            return count
from collections import defaultdict
class Solution:
      def countCompleteSubarrays(self, nums: list[int]) -> int:
            k=len(set(nums))
            count=0
            for i in range(len(nums)):
                hash_map=defaultdict(int)
                hash_map[nums[i]]=1
                for j in range(i,len(nums)):
                    hash_map[nums[j]]+=1
                    if len(hash_map)==k:
                       count+=1 
            return count
class TestApp:
    def testing_one_case(self):
        assert Solution().countCompleteSubarrays([1,3,1,2,2])==4 
    def testing_two_case(self):
        assert Solution().countCompleteSubarrays([5,5,5,5])==10