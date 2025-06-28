class Solution:
      def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
          paragraph=paragraph.replace("!","").replace("?","").replace("'","").replace(",","").replace(";","").replace(".","")
          paragraph=paragraph.lower()
          paragraph=paragraph.split(" ")
          hash_map={}
          for word in paragraph:
              if word:
                 if word not in hash_map:
                     hash_map[word]=1
                 else:
                     hash_map[word]+=1
          hash_map=list(hash_map.items())
          hash_map.sort(reverse=True,key=lambda x:x[1])
          for word in hash_map:
              if word[0] not in banned:
                  return word[0]
class TestApp:
      def testing_case_one(self):
          assert Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"])=="ball"
      def testing_case_two(self):
          assert Solution().mostCommonWord("a.",[])=="a"
          