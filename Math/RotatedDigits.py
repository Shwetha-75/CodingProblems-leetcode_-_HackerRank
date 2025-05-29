class Solution:
      def rotatedDigits(self, n: int) -> int:
          count=0 
        #  digits are valid if and only if it as 2,5,6,9 
          for i in range(1,n+1):
              if self.helper(i):
                  count+=1 
          return count
      def helper(self,number:int):
          valid=False 
          while number:
                rem=number%10 
                if rem==2 or rem==5 or rem==6 or rem==9:
                    valid=True 
                elif rem==3 or rem==4 or rem==7:
                    valid=False 
                number//=10 
          return  valid