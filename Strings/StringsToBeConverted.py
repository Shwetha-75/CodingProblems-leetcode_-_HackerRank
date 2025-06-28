class Solution:
      def rotateString(self, s: str, goal: str) -> bool:
          goal+=goal 
          return s in goal