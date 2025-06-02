class Solution:
      def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        row=len(mat)
        col=len(mat[0])
        result=[]
        for line in range(1,row+col):
            startCol=max(0,line-row)
            count=min(line,col-startCol,col)
            temp=[]
            for j in range(count):
                m=min(line,row)-j-1
                n=startCol+j 
                temp.append(mat[m][n])
            
            if line%2:
               result.append(temp[:])
            else:
                result.append(temp[::-1])
        return result
       