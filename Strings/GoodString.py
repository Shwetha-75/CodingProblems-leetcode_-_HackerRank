'''
Given a string s of length N, you have to tell whether it is good or not. A good string is one where the distance between every two adjacent character is exactly 1. Here distance is defined by minimum distance between two character when alphabets from 'a' to 'z' are put in cyclic manner. For example distance between 'a' to 'c' is 2 and distance between 'a' to 'y' is also 2. The task is to return "YES" or "NO" (without quotes) depending on whether the given string is Good or not.

Note: Unit length string will be always good.

Example 1:

Input: s = "aaa"
Output: NO
Explanation: distance between 'a' and 'a' is not 1.
Example 2:

Input: s = "cbc"
Output: YES
Explanation: distance between 'b' and 'c' is 1.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function isGoodString() which accepts a string as input parameter and returns "YES" or "NO" (without quotes) accordingly. 
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
String contains only lower case english alphabets.

1 <= N <= 105

'''


class Solution:
      def isGoodString(self,s:str)->str:
          for i in range(len(s)-1):
              if s[i]=='a' and s[i+1]=='z' or s[i]=='z' and s[i+1]=='a':
                  continue
              
              if abs(ord(s[i])-ord(s[i+1]))!=1:
                 return "NO" 
          return "YES"

class TestApp:
      def testing_case_one(self):
          assert Solution().isGoodString("aaa")=="NO"
      def testing_case_two(self):
          assert Solution().isGoodString("cbc")=="YES"
      def testing_case_three(self):
          assert Solution().isGoodString("zab")=="YES"
      def testing_case_four(self):
          assert Solution().isGoodString("az")=="YES"