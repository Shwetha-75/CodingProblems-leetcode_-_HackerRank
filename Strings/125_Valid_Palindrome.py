import re 

class Solution:
      def isPalindrome(self, s: str) -> bool:
          s=s.lower()
          s=re.findall("[a-z0-9]",s) 
          left,right=0,len(s)-1 
          while left <=right :
                if s[left]!=s[right]:
                    return False 
                left+=1 
                right-=1
          return True 
      
class Solution:
      def isPalindrome(self, s: str) -> bool:
          s=s.lower()
          left,right=0,len(s)-1
          while left<=right:
                if not s[left].isalnum():
                    left+=1 
                    continue 
                if not s[right].isalnum():
                    right-=1 
                    continue 
                if s[left]!=s[right]:
                    return False 
                left+=1 
                right-=1 
          return True 

class TestApp:
      def testing_case_one(self):
          assert Solution().isPalindrome("A man, a plan, a canal: Panama")==True 
      def testing_case_two(self):
          assert Solution().isPalindrome("race a car")==False 
      def testing_case_three(self):
          assert Solution().isPalindrome(" ")==True 
      def testing_case_four(self):
          assert Solution().isPalindrome("0P")==False 
      def testing_case_five(self):
          assert Solution().isPalindrome("abb")==False