class Solution:
      def balancedStringSplit(self, s: str) -> int:
            
            count=0
            hash_map={}
            for j in range(len(s)):
                if s[j] not in hash_map:
                    hash_map[s[j]]=1
                else:
                    hash_map[s[j]]+=1 
                if 'L' in hash_map and 'R' in hash_map and hash_map['L']==hash_map['R']:
                   count+=1
                   hash_map={} 
            return  count
class TestApp:
      def testing_case_one(self):
          assert Solution().balancedStringSplit("RLRRLLRLRL")==4
      def testing_case_two(self):
          assert Solution().balancedStringSplit("RLRRRLLRLL")==2