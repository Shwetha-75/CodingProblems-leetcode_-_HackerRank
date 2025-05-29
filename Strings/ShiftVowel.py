class Solution:
      def reverseVowels(self, s: str) -> str:
          vowels={'a':1,'e':1,'i':1,'o':1,'u':1,'A':1,'E':1,'I':1,'O':1,'U':1}
          s=list(s)
          
          left,right=0,len(s)-1 
          while left<=right:
                while left<len(s) and s[left] not in vowels:
                      left+=1 
                while right>=0 and s[right] not in vowels:
                    right-=1 
                if left<=right:
                   s[left],s[right]=s[right],s[left]
                   left+=1
                   right-=1 
          return ''.join(s)
class TestApp:
      def testing_case_one(self):
          assert Solution().reverseVowels("IceCreAm")=="AceCreIm"
      def testing_case_two(self):
          assert Solution().reverseVowels("leetcode")=="leotcede"
     