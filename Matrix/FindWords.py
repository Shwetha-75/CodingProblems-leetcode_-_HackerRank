from collections import Counter

class Solution:
      def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
            result=[]
            for i in range(len(board)):
                board[i]=dict(Counter(board[i]))
            for word in words:
                length=0
                flag=False 
                count=0
                temp=board[::]
                k_index=0
                while k_index<len(word):
                    for index in range(len(temp)):
                        if word[k_index] in temp[index] and temp[index][word[k_index]]>0:
                            flag=True
                            temp[index][word[k_index]]-=1 
                            length+=1
                            k_index+=1
                            
                            break 
                        elif flag:
                            count+=1
                        print(word[k_index],temp[index],count)
                        if count>=2:
                            break 
                    # print(temp)
                    if count>=2 or not flag:
                       break 
                    
                        
                if len(word)==length:
                    result.append(word)
            return result 
Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"])
class TestApp:
      def testing_case_one(self):
          assert Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"])==["eat","oath"] 
              