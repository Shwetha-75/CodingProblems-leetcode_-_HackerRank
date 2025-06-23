'''
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.
 

Example 1:


Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
Example 2:

Input: points = [[3,2],[-2,2]]
Output: 5
 

Constraints:

points.length == n
1 <= n <= 100
points[i].length == 2
-1000 <= points[i][0], points[i][1] <= 1000

'''

class Solution: 

        def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
            count=0
            n=len(points)
            for i in range(1,n):
                prev,curr=points[i-1],points[i]
                m1,m2=min(prev),min(curr)
                if m1<m2:
                    count+=self.helper(prev,curr,m2)
                else:
                    count+=self.helper(curr,prev,m1)
            return count
                    
                
        def helper(self,prev:list[int],curr:list[int],m2:int):
                count=0
                while prev[0]<m2 and prev[1]<m2:
                    prev[0]+=1
                    prev[1]+=1
                    count+=1
                diff1=abs(prev[0]-curr[0])
                diff2=abs(prev[1]-curr[1])
                if diff1==diff2:
                   count+=diff1 
                else:
                    count+=diff1+diff2  
               
                return count 
class Solution:
      def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
          count=0 
          n=len(points)
          for i in range(1,n):
              count+=max(abs(points[i-1][0]-points[i][0]),abs(points[i-1][1]-points[i][1]))
          return count
      
# Solution().minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]) 
class TestApp:
      def testing_case_one(self):
          assert Solution().minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])==7 
      def testing_case_two(self):
          assert Solution().minTimeToVisitAllPoints([[3,2],[-2,2]])==5   