class Solution:
      def helper(self,number):
          value=0
        #   count the digits 
          temp=number 
          count=0 
          while temp:
                count+=1
                temp//=10 
          pow=count-1
        
          while number!=0:
                rem=number%10 
                value+=rem*10**pow
                number//=10
                pow-=1 
          return value 
      def checkPalindromeNumber(self,number:int):
          return False if number<0 else True if number==self.helper(number) else False 

class TestApp:
      def testing_case_one(self):
          assert Solution().checkPalindromeNumber(121)==True 
      def testing_case_two(self):
          assert Solution().checkPalindromeNumber(123)==False 
      def testing_case_three(self):
          assert Solution().checkPalindromeNumber(12321)==True 