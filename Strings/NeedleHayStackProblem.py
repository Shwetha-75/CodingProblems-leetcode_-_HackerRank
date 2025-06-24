class Solution:
      def strStr(self, haystack: str, needle: str) -> int:
          if len(haystack)<len(needle):
              return -1
          for i in range(len(haystack)):
              for j in range(i,len(haystack)):
                  if len(haystack[i:j+1:])>len(needle): break
                  if haystack[i:j+1:]==needle:
                     return i 
          return -1
class Solution:
      def strStr(self, haystack: str, needle: str) -> int:
          return haystack.index(needle) if needle in haystack else -1           

class TestApp:
      def testing_case_one(self):
          assert Solution().strStr("sadbutsad","sad")==0
      def testing_case_two(self):
          assert Solution().strStr("leetcode","leeto")==-1
      def testing_case_three(self):
          assert Solution().strStr("hello","ll")==2
      def testing_case_four(self):
          assert Solution().strStr("mississippi","issip")==4
      def testing_case_five(self):
          assert Solution().strStr("sadbutsad","sad")==0
      def testing_case_six(self):
          assert Solution().strStr("a","a")==0
          
     
    