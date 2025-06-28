from collections import defaultdict

# Brute Force Approach

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort(key=lambda x:x[1 ])
        hash_map=defaultdict(int)
        for event in events:
            for day in range(event[0],event[1]+1):
                if day not in hash_map:
                    hash_map[day]+=1
                    break
        return len(hash_map.keys())
# Wrong Approach
class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:    
        events.sort(key=lambda x:x[1])
        stack=[events[0][0]]
        for i in range(1,len(events)):
            if stack[-1]+1>=events[i][0] and stack[-1]+1<=events[i][1]:
               stack.append(stack[-1]+1)
        return len(stack) 
                

class TestApp:
      def testing_case_one(self):
          assert Solution().maxEvents([[1,2],[2,3],[3,4]])==3
      def testing_case_two(self):
          assert Solution().maxEvents([[1,2],[2,3],[3,4],[1,2]])==4
      def testing_case_three(self):
          assert Solution().maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]])==4
      def testing_case_four(self):
          assert Solution().maxEvents([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]])==7