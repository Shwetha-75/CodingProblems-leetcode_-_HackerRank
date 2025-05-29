class Solution:
        def gcdOfStrings(self, str1: str, str2: str) -> str:
            t,s='',''
            if len(str1)>len(str2):
                s=str1
                t=str2 
            else:
                s=str2
                t=str1 
            temp=""
            value=""
            for char in t:
                temp+=char 
               
                if len("".join(s.split(temp)))==0 and len("".join(t.split(temp)))==0:
                   if len(value)<=len(temp):
                       value=temp 
            return value 
class TestApp:
      def testing_case_one(self):
          assert Solution().gcdOfStrings("ABCABC","ABC")=="ABC"
      def testing_case_two(self): 
          assert Solution().gcdOfStrings("ABABAB","ABAB")=="AB"
      def testing_case_three(self):
          assert Solution().gcdOfStrings("LEET","CODE")==""
      def testing_case_four(self):
          assert Solution().gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX","TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")=="TAUXX"
      def testing_case_five(self):
          assert Solution().gcdOfStrings("ABABABAB","ABAB")=="ABAB"