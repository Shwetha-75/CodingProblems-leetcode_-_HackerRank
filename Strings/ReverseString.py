class Solution:
      def rotateString(self,s:str):
          return (" ".join([word for word in s.split(" ") if word and word!=' '][::-1])).rstrip().lstrip()

class TestApp:
      def testing_case_one(self):
          assert Solution().rotateString("the sky is blue")=="blue is sky the"
      def testing_case_two(self):
          assert Solution().rotateString(" hello world  ")=="world hello"