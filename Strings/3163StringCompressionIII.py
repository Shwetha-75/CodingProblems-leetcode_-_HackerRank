class Solution:
      def compressedString(self, word: str) -> str:
            stack=[]
            hash_map={word[0]:1}
            for i in range(1,len(word)):
                  if word[i] in hash_map and hash_map[word[i]]>=9:
                     stack.append(str(hash_map[word[i]]))
                     stack.append(word[i])
                     hash_map[word[i]]=1 
                  elif word[i] not in hash_map:
                      stack.append(str(hash_map[word[i-1]]))
                      stack.append(word[i-1])
                      hash_map[word[i]]=1
                  else:
                      hash_map[word[i]]+=1 
            stack.append(str(hash_map[word[-1]]))
            stack.append(word[-1])
            return "".join(stack)

class TestApp:
      def testing_case_one(self):
          assert Solution().compressedString("abcde")=="1a1b1c1d1e"
          
      def testing_case_two(self):
          assert Solution().compressedString("aaaaaaaaaaaaaabb")=="9a5a2b"