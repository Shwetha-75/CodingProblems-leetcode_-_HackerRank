class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        result=[]
        for i in range(2,len(len(text))):
            if first==text[i-2] and second==text[i-1]:
                result.append(text[i])
        return result