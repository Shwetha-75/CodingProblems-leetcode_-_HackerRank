class Solution:
      def licenseKeyFormatting(self, s: str, k: int) -> str:
        #   convert all the lower case to Upper case 
        s=s.replace("-","")
        s=list(s)[::-1]
        for i in range(len(s)):
            if ord(s[i])>=97 and ord(s[i])<=122:
               s[i]=chr(ord(s[i])-32)
        start=0
        result=[]
        while start<len(s):
              end=min(len(s),start+k)
              result+=s[start:end]
              result.append("-")
              start+=k
        return "".join(result[::-1])[1::]
Solution().licenseKeyFormatting("2-5g-3-J",2)