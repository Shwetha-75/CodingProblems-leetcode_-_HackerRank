class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count=0
        value=min(limit,n)
        for i in range(value+1):
            count+=max(min(limit,n-i)-max(0,n-i-limit)+1,0)
        return count 
class TestApp:
      def testingCaseOne(self):
          assert Solution().distributeCandies(3,3)==10 
      def testingCaseTwo(self):
          assert Solution().distributeCandies(5,2)==3