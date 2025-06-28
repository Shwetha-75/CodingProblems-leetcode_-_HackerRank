from collections import defaultdict
class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        used=defaultdict(int)
        k=[i for i in range(-k,k+1)]
        for num in nums:
            
            for value in k:
                if num-value not in used:
                    used[num-value]+=1 
                    break
        return len(used.keys())
class TestApp:
      def testing_case_one(self):
          assert Solution().maxDistinctElements([1,2,2,3,3,4],2)==6 
      def testing_case_two(self):
          assert Solution().maxDistinctElements([4,4,4,4],1)==3