import math
class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        for i in range(1,10**7):
            total=0
            for j in range(len(dist)-1):
                total+=math.ceil(dist[j]/i)
            total+=dist[len(dist)-1]/i
            
            if total<=hour:
                return i 
        return -1
# binary Search 
class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        low,high=1,10**7 
        result=-1 
        while low<=high:
              speed=low+(high-low)//2
              total=0 
              for i in range(len(dist)-1):
                  total+=math.ceil(dist[i]/speed)
              total+=dist[-1]/speed
              if total<=hour:
                result=speed 
                high=speed-1
              else:
                  low=speed+1 
        return result
class TestApp:
      def testing_case_one(self):
          assert Solution().minSpeedOnTime([1,3,2],6)==1 
      def testing_case_two(self):
          assert Solution().minSpeedOnTime([1,3,2],2.7)==3 
      def testing_case_three(self):
          assert Solution().minSpeedOnTime([1,3,2],1.9)==-1