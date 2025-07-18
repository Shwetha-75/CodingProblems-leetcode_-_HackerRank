'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

'''
class Solution:
      def pascalTriangle(self,row:int):
            result=[]
            for i in range(1,row+2):
                temp=[1]*i
                if i>2:
                    for j in range(1,i-1):
                        temp[j]=result[-1][j-1]+result[-1][j]
                result.append(temp)
            return result[-1]
class TestApp:
      def testing_case_one(self):
          assert Solution().pascalTriangle(3)==[1,3,3,1]
      def testing_case_two(self):
          assert Solution().pascalTriangle(1)==[1,1]
      def testing_case_three(self):
          assert Solution().pascalTriangle(0)==[1]
          
