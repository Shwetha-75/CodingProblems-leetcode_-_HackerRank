from collections import defaultdict
class Solution:
      def countCompleteSubarrays(self, nums: list[int]) -> int:
          count=0 
          distinct=len(set(nums))
          for i in range(len(nums)):
              hash_map=defaultdict(int)
              for j in range(i,len(nums)):
                  hash_map[nums[j]]+=1 
                  if len(hash_map)>=distinct:
                     count+=1 
          return count
class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        count=start=end=0
        hash_map=defaultdict(int)
        distinct=len(set(nums))
        while end<len(nums):
              if start>0:
                 hash_map[nums[start-1]]-=1 
                 if hash_map[nums[start-1]]==0:
                     del hash_map[nums[start-1]]
              while end<len(nums) and len(hash_map)<distinct:
                    hash_map[nums[end]]+=1
                    end+=1 
              if len(hash_map)==distinct:
                 count+=len(nums)-end+1
              start+=1 
              
        return count

class TestApp:
      def testing_case_one(self):
          assert Solution().countCompleteSubarrays([1,3,1,2,2])==4
      def testing_case_two(self):
          assert Solution().countCompleteSubarrays([5,5,5,5])==10