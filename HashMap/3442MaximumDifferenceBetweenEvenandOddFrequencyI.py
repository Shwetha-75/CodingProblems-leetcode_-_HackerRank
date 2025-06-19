class Solution:
    def maxDifference(self, s: str) -> int:
        hash_map={}
        for char in s:
            if char not in hash_map:
                hash_map[char]=1
            else:
                hash_map[char]+=1
        hash_map=list(hash_map.items())
        hash_map.sort(reverse=True,key= lambda x:x[1])
        odd_hash_map=[value[1]  for value in hash_map if value[1]%2]
        even_hash_map=[value[1] for value in hash_map if not value[1]%2]
        return odd_hash_map[0]-even_hash_map[-1]
class TestApp:
      def testing_case_one(self):
          assert Solution().maxDifference("aaaaabbc")==3
      def testing_casE_two(self):
          assert Solution().maxDifference("abcabcab")==1