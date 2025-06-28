'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''

class Solution:
      def longestCommonPrefix(self, strs: list[str]) -> str:
          longest_string=""
          word=strs[0]
          for i in range(len(strs[0])):
              temp=word[:i+1:]
              for j in range(1,len(strs)):
                
                  if temp!=strs[j][:i+1:]:
                     return longest_string 
              if len(longest_string)<len(temp):
                  longest_string=temp 
          return longest_string 
class TestApp:
      def testing_case_one(self):
          assert Solution().longestCommonPrefix(["flower","flow","flight"])=="fl"
      def testing_case_two(self):
          assert Solution().longestCommonPrefix(["dog","racecar","car"])==""