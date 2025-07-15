'''
Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

 

Example 1:

Input: n = 3
Output: 3
Example 2:

Input: n = 11
Output: 0
Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
 

Constraints:

1 <= n <= 231 - 1

'''
class Solution:
    def findNthDigit(self, n: int) -> int:
        if n<=9:
            return n 
        base,digits=9,1
        while n>base*digits:
              n-=base*digits 
              base*=10
              digits+=1
        number=10**(digits-1)+(n-1)//digits 
        index=(n-1)%digits 
        return int(str(number)[index])
class TestApp:
      def testing_case_one(self):
          assert Solution().findNthDigit(3)==3
      def testing_case_two(self):
          assert Solution().findNthDigit(13)==1
      def testing_case_three(self):
          assert Solution().findNthDigit(15)==2
      def testing_case_four(self):
          assert Solution().findNthDigit(21)==5
    