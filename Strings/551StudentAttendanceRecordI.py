class Solution:
    def checkRecord(self, s: str) -> bool:
        count_l=s.count('A')
        for i in range(1,len(s)-1):
            if s[i-1]==s[i]==s[i+1]=='L' and count_l>=2:
                return False 
        return True