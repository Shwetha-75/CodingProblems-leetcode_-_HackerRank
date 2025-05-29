class Solution:
      def makeTheURL(self,s1:str,n:int)->str:
          stack=[]
          index=0 
          while index<n:
                if s1[index]==' ' and stack and stack[-1]!="%20":
                   stack.append("%20")
                elif s1[index]!=' ':
                    stack.append(s1[index])
                index+=1 
          return ''.join(stack)

class TestApp:
      def testing_case_one(self):
          assert Solution().makeTheURL("Mr 3ohn Smith       ",13)=="Mr%203ohn%20Smith"
      
      def testing_case_two(self):
          assert Solution().makeTheURL("Miss Shwetha K, she is unstoppable",34)=="Miss%20Shwetha%20K,%20she%20is%20unstoppable"
      