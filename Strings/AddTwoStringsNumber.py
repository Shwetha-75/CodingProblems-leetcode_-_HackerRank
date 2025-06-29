import sys
'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.

'''
class Solution:
      def charVal(self,char):
          return "0123456789".index(char) 
      def addTwoNumber(self,number:str):
          val=pow=0
          index=len(number)-1 
          while index>=0:
                val+=self.charVal(number[index])*10**pow 
                index-=1 
                pow+=1 
          return val 
      def addStrings(self, num1: str, num2: str) -> str:
          # to increase the limit    
          sys.set_int_max_str_digits(100000)
          return self.addStrings(num1)+self.addStrings(num2)  
        