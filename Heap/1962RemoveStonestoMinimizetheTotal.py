import heapq
import math
class Solution:
      def minStoneSum(self, piles: list[int], k: int) -> int:
          piles=[-1*pile for pile in piles]
          heapq.heapify(piles)
          while k:
                temp=abs(heapq.heappop(piles))
                heapq.heappush(piles,-1*math.ceil(temp/2))
                k-=1
          return -1*sum(piles)
class TestApp:
      def testing_case_one(self):
          assert Solution().minStoneSum([5,4,9],2)==12
      def testing_case_two(self):
          assert Solution().minStoneSum([4,3,6,7],3)==12