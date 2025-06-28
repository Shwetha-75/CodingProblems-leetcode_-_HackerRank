class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        max_diff=-1
        n=len(colors)
        for i in range(n):
            temp=-1
            for j in range(i+1,n):
                if colors[i]!=colors[j]:
                   temp=max(temp,j-i)
            max_diff=max(max_diff,temp)
        return max_diff 
class TestApp:
      def testing_case_one(self):
          assert Solution().maxDistance([1,8,3,8,3])==4 
      def testing_case_two(self):
          assert Solution().maxDistance([0,1])==1
      def testing_case_three(self):
          assert Solution().maxDistance([1,1,1,6,1,1,1])==3
      def testing_case_four(self):
          assert Solution().maxDistance([100,0])==1