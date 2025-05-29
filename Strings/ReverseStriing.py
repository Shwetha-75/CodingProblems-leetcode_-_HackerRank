class Solution:
      def reverseStr(self,s:str,k:int):
          s=list(s)
          for i in range(0,len(s),2*k):
              j=min(i+k-1,len(s)-1)
              print(i,j)
              while i<j:
                    s[i],s[j]=s[j],s[i]
                    i+=1
                    j-=1
              print(i,j)
Solution().reverseStr("abcdefgh",2)     