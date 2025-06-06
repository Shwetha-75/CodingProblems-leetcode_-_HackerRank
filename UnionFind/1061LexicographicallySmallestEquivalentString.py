import heapq
class Solution:
    def __init__(self):
        self.array=list(range(26))
    def find(self,code):
        if self.array[code]==code:
            return code 
        return self.find(self.array[code])
    def union(self,code1,code2):
        left=self.find(code1) 
        right=self.find(code2)
        self.array[max(left,right)]=min(left,right)
        
    def smallestEquivalentString(self, s1: str, s2: str="", baseStr: str="") -> str:
        for i in range(len(s1)):
            self.union(ord(s1[i])-97,ord(s2[i])-97)
        baseStr=list(baseStr)
        for i in range(len(baseStr)):
            baseStr[i]=chr(97+self.find(ord(baseStr[i])-97))
        return "".join(baseStr)

class TestApp:
    def testing_case_one(self):
        assert  Solution().smallestEquivalentString("parker","morris","parser")=="makkek"
    def testing_case_two(self):
        assert Solution().smallestEquivalentString("leetcode","programs","sourcecode")=="aauaaaaada"
        
            
                    