class Solution:
      def compressString(self,string:str)->str:
          stack=[]
          freq=[0]*26 
          for char in string:
              if not stack :
                  stack.append(char)
                  
              elif stack and stack[-1]!=char:
                  stack.append(char)
              freq[ord(char)-97]+=1 
          if len(stack)==len(string):
              return string 
          result=[]
          for char in stack:
              result.append(char+str(freq[ord(char)-97]))
          return "".join(result)


class TestApp:
      def testing_case_one(self):
          assert Solution().compressString("abcd")=="abcd"
      def testing_case_two(self):
          assert Solution().compressString("aaabbbcccdd")=="a3b3c3d2"
      def testing_case_three(self):
          assert Solution().compressString("aabbccd")=="a2b2c2d1"
          