class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        stack=[[0,groups[0]]]
        for i in range(1,len(groups)):
            if stack[-1][-1] != groups[i]:
               stack.append([i,groups[i]])
        return [words[arr[0]] for arr in stack]
class TestApp:
      def testing_case_one(self):
          assert Solution().getLongestSubsequence(["e","a","b"],[0,0,1])==["e","b"]
      def testing_case_two(self):
          assert Solution().getLongestSubsequence(["a","b","c","d"],[1,0,1,1])==["a","b","c"]