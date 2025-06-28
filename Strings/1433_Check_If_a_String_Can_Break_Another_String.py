class Solution:
      def checkIfCanBreak(self, s1: str, s2: str) -> bool:  
          if len(s1)!=len(s2): return False 
          s1=sorted(s1)
          s2=sorted(s2)
          index=0 
          flag=True 
          while index<len(s1):
                if not s1[index]>=s2[index]:
                    flag=False 
                    break
                index+=1 
          if not flag: return True
          index=0
          while index<len(s1):
                if not  s2[index]>=s1[index]:
                    return False 
                index+=1
          return True  


class TestApp:
      def testing_case_one(self):
          assert Solution().checkIfCanBreak("abc","xya")==True 
      def testing_case_two(self):
          assert Solution().checkIfCanBreak("abe","acd")==False 
      def testing_case_three(self):
          assert Solution().checkIfCanBreak("leetcodee","interview")==True 