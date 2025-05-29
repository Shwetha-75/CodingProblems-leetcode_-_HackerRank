from collections import Counter
class Solution:
        def commonChars(self, words: list[str]) -> list[str]:
            temp=[dict(Counter(words[i])) for i in range(1,len(words))]
            result=[]
            for character in words[0]:
                flag=True 
                for word in temp:
                    if character not in word:
                       flag=False 
                    else:
                        word[character]-=1
                        if word[character]==0:
                           del word[character]
                if flag:
                   result.append(character)
            return result 
class TestApp:
      def testing_case_one(self):
          assert Solution().commonChars(["bella","label","roller"])==['e','l','l']
      def testing_case_two(self):
          assert Solution().commonChars(["cool","lock","cook"])==['c','o']
    