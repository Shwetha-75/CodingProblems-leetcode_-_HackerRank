from collections import defaultdict
class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        hash_map=defaultdict(int)
        for i in candyType:
            hash_map[i]+=1 
        mid=len(candyType)//2 
        return min(mid,len(hash_map.keys()))
    
class TestApp:
      def testing_case_one(self):
          assert Solution().distributeCandies([1,1,2,3])==2 
      def testing_case_two(self):
          assert Solution().distributeCandies([6,6,6,6,6])==1 
      def testing_case_three(self):
          assert Solution().distributeCandies([1,1,2,2,3,3,4])==3