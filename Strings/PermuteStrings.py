class Solution:
      def customSortString(self, order: str, s: str) -> str:
            hash_map={}
            result=[]
            for char in s:
                if char in hash_map:
                    hash_map[char]+=1
                else:hash_map[char]=1
            for char in order:
                if char in hash_map:
                    result+=[char]*hash_map[char]
                    del hash_map[char]
            for key,value in hash_map.items():
                result+=[key]*value
            return "".join(result)
class TestApp:    
      def testing_case_one(self):
          assert Solution().customSortString("cba","abcd")=="cbad"
      def testing_case_two(self):
          assert Solution().customSortString("bcafg","abcd")=="bcad"
      def testing_case_three(self):
          assert Solution().customSortString("kqep","pekeq")=="kqeep"