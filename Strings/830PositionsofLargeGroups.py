class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        result=[]
        start,end=0,0
        flag=False
        while end<len(s):
            if s[start]!=s[end]:
             
                if end-start >=3:
                   result.append([start,end-1])
                   result
                start=end 
            end+=1 
        if start!=end and end-start>=3:
           result.append([start,end-1])
            
        return result 
class TestApp:
      def testing_case_one(self):
          assert Solution().largeGroupPositions("abbxxxxzzy")==[[3,6]]
      def testing_case_two(self):
          assert Solution().largeGroupPositions("abc")==[]
      def testing_case_three(self):
          assert Solution().largeGroupPositions("abcdddeeeeaabbbcd")==[[3,5],[6,9],[12,14]]
      def testing_case_four(self):
          assert Solution().largeGroupPositions("aaa")==[[0,2]]
      def testing_case_five(self):
          assert Solution().largeGroupPositions("aabbbccccccc")==[[2,4],[5,11]]