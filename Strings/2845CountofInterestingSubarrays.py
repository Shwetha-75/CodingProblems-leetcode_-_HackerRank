from collections import defaultdict
class Solution:
        def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
            count=0 
            n=len(nums)
            for i in range(n):
                cnt=0
                for j in range(i,n):
                    if nums[j]%modulo==k:
                       cnt+=1 
                    if cnt%modulo==k:
                        count+=1 
            return count 
class Solution:
      def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
          hash_map=defaultdict(int)
          hash_map[0]=1
          prefix=count=0 
          for num in nums:
              prefix+=1 if num%modulo==k else 0 
              count+=hash_map[(prefix+modulo-k)%modulo]
              hash_map[prefix%modulo]+=1 

          return  count            
              
class TestApp:
      def testing_case_one(self):
          assert Solution().countInterestingSubarrays([3,2,4],2,1)==3 
      def testing_case_two(self):
          assert Solution().countInterestingSubarrays([3,1,9,6],3,0)==2