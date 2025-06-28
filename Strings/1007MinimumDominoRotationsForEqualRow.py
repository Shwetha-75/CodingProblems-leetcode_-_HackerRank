from collections import Counter
class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        hash_map_top=dict(Counter(tops))
        hash_map_bottom=dict(Counter(bottoms))
        max_top=max(hash_map_top.items(),key=lambda x:x[1])
        max_bottom=max(hash_map_bottom.items(),key=lambda x:x[1])
        if max_top[1]>max_bottom[1]:
           count=len(tops)-max_top[1]
           for i in range(len(tops)):
               if tops[i]!=max_top[0] and bottoms[i]==max_top[0]:
                   tops[i]=max_top[0]
                   count-=1 
     
           if count<=0:
               return len(tops)-max_top[1]
        count=len(bottoms)-max_bottom[1]
        for i in range(len(bottoms)):
            if bottoms[i]!=max_bottom[0] and tops[i]==max_bottom[0]:
                count-=1 
        if count<=0:
            return len(bottoms)-max_bottom[1]
        return -1 
    
# Optimized Approach 
from collections import defaultdict
class Solution:
        def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
            if len(tops)!=len(bottoms):
                return -1
            count_top=defaultdict(int)
            count_bottom=defaultdict(int)
            same=0 
            for i in range(len(tops)):
                count_top[tops[i]]+=1 
                count_bottom[bottoms[i]]+=1 
                if tops[i]==bottoms[i]:
                    same+=1 
            for i in range(1,7):
                if count_top[i]+count_bottom[i]-same==len(tops):
                    return len(tops)-max(count_top[i],count_bottom[i])
            return -1

class TestApp:
      def testing_case_one(self):
          assert Solution().minDominoRotations([2,1,2,4,2,2],[5,2,6,2,3,2])==2 
      def testing_case_two(Self):
          assert Solution().minDominoRotations([3,5,1,2,3],[3,6,3,3,4])==-1
            
