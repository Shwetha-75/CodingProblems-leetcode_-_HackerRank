class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr=[0]*26 
        for letter in s:
            arr[ord(letter)-97]+=1 
        for i in range(len(s)):
            if arr[ord(s[i])-97]==1:
                return i 
        return -1 
class TestApp:
      def testing_case_one(self):
          assert Solution().firstUniqChar("leetcode")==0
      def testing_case_two(self):
          assert Solution().firstUniqChar("testing")==1 
      def testing_case_three(self):
          assert Solution().firstUniqChar("dadada")==-1 
      def testing_case_four(self):
          assert Solution().firstUniqChar("aaaaaaaaa")==-1