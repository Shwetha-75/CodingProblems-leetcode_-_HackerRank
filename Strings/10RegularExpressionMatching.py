class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        index_1,index_2=0,0 
        while index_1<len(s) and index_2<len(p):
            if p[index_2]=='.':
                index_1+=1 
                index_2+=1
            elif p[index_2]=='*':
                return True 
            elif p[index_2]==s[index_1]:
                 index_1+=1 
                 index_2+=1 
        return False if index_1<len(s) or index_2<len(p) else True 
class TestApp:
      def testing_case_one(self):
          assert Solution().isMatch("aa","a")==False 
      def testing_case_two(self):
          assert Solution().isMatch("aa","a*")==True 
      def testing_case_three(self):
          assert Solution().isMatch("ab",".*")==True 
        