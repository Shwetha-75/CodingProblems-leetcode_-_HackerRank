class Solution:
      def lengthLongestPath(self, input: str) -> int:
          input=input.replace("\n",'-').replace("\t","@")
          print(input)
Solution().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")