class Solution:
      def longestStrChain(self, words: list[str]) -> int:
            result=1 
            words.sort(key=lambda x:len(x))
            for i in range(1,len(words)):
                for j in range(i-1,-1,-1):
                    prev=words[j]
                    curr=words[i]
                    index_1=index_2=count=0 
                    if len(curr)-len(prev)<=1:
                        while index_1<len(prev) and index_2<len(curr):
                            if count>1:
                                break 
                            if prev[index_1]==curr[index_2]:
                                index_1+=1 
                            else:
                                count+=1
                            index_2+=1 
                        if count<=1 and index_1==len(prev):
                            result+=1 
                            break
                    else:
                        break 
            print(result)                                
            return result 

Solution().longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"])
class TestApp:
        def testing_case_one(self):
            assert Solution().longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"])==5 
        def testing_case_two(self):
            assert Solution().longestStrChain(["a","b","ba","bca","bda","bdca"])==4 
        def testing_case_three(self):
            assert Solution().longestStrChain(["abcd","dbqca"])==1 
        def testing_case_four(self):
            assert Solution().longestStrChain(["bdca","bda","ca","dca","a"])==4
