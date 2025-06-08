from itertools import permutations
class Solution:

      def numTilePossibilities(self, tiles: str) -> int:
            result=set()
            total=2**len(tiles)
            n=len(tiles)
            for count in range(1,total):
                temp=[]
                for i in range(n):
                    if count & 1<<i:
                       temp.append(tiles[i])
                temp="".join(temp)
                perm=permutations(temp)
                for char in perm:
                    result.add("".join(char))
            
            return len(result)
Solution().numTilePossibilities("ABC")
class TestApp:
      def testing_case_one(self):
          assert Solution().numTilePossibilities("AAB")==8
      def testing_case_two(self):
          assert Solution().numTilePossibilities("AAABBC")==188
      def testing_case_three(self):
          assert Solution().numTilePossibilities("ABC")==15
          