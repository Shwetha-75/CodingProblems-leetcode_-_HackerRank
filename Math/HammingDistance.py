class Solution:
      def hammingDistance(self, x: int, y: int) -> int:
          x:list[str]=list(str(bin(x))[2::])
          y:list[str]=list(str(bin(y))[2::])
          if len(x)<len(y):
             while len(x)<len(y):
                   x=[0]+x 
             
          elif len(y)<len(x):
               while len(y)<len(x):
                   y=['0']+y 
          count=0
          index=0 
          while index<len(y):
                if x[index]!=y[index]:
                    count+=1
                index+=1
          print(x)
          print(y)
          return count
Solution().hammingDistance(4,1)

