class Solution:
      def repeatedCharacter(self, s: str) -> str:
          freq=[0]*26 
          indices=[[] for _ in range(26)]
          for i in range(len(s)):
              index=ord(s[i])-97
              freq[index]+=1 
              indices[index].append(i)
          value=float('inf')
          char=''
          for i in range(len(s)):
              index=ord(s[i])-97 
              if freq[index]>=2:
                  if indices[index][1]<value:
                      value=indices[index][1]
               
                      char=s[i]
          return char 
      
class TestApp:
      def testing_case_one(self):
          assert Solution().repeatedCharacter("abccbaacz")=="c"
      def testing_case_two(self):
          assert Solution().repeatedCharacter("abcdd")=="d"