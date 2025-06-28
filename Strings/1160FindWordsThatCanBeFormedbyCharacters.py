from collections import Counter
class Solution:
      def countCharacters(self, words: list[str], chars: str) -> int:
            chars=dict(Counter(chars))
            count=0
            for word in words:
                hash_map=dict(Counter(word))
                flag=True 
                for key,value in hash_map.items():
                    if key not in chars or value>chars[key]:
                        flag=False 
                        break 
                if flag:
                   count+=len(word)
            return count 
class TestApp:
      def testing_case_one(self):
          assert Solution().countCharacters(["cat","bt","hat","tree"],"atach")==6 
      def testing_case_two(self):
          assert Solution().countCharacters(["hello","world","leetcode"],"welldonehoneyr")==10