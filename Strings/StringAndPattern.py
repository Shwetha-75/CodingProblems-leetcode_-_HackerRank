class Solution:
      def wordPattern(self, pattern: str, s: str) -> bool:
          word_map={}
          letter_map={}
          i=j=0 
          words=s.split(" ")
          while i<len(words) and j<len(pattern):
                if pattern[j] not in letter_map and words[i] not in word_map:
                   letter_map[pattern[j]]=words[i]
                   word_map[words[i]]=pattern[j]
                   i+=1
                   j+=1
                   continue 
                if words[i] in word_map:
                   i+=1
                if pattern[j] in letter_map:
                    j+=1
          return i>=len(words)
class TestApp:
      def testing_case_one(self):
          assert Solution().wordPattern("abba","dog cat cat dog")==True 
      def testing_case_two(self):
          assert Solution().wordPattern("abba","dog cat cat fish")==False 
      def testing_case_three(self):
          assert Solution().wordPattern("aaaa","dog cat cat dog")==False
