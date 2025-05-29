class Solution:
      def checkPalindrome(self,string:str)->bool:
            freq=[0]*26
            for char in string:
                freq[ord(char)-97]+=1 
            # checking the frequency count 
            oddFreq=False 
            for count in freq:
                if count%2==1:
                    if oddFreq: return False 
                    oddFreq=True 
            return True 
class TestApp:
      def testing_case_one(self):
          assert Solution().checkPalindrome("mom")==True 
      def testing_case_two(self):
          assert Solution().checkPalindrome("loolol")==False
      def testing_case_three(self):
          assert Solution().checkPalindrome("loolool")==True
      def testing_case_four(self):
          assert Solution().checkPalindrome("momommomom")==True 
      def testing_case_five(self):
          assert Solution().checkPalindrome("")
               