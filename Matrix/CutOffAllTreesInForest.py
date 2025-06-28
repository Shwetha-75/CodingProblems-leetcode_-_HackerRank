class Solution:
    def cutOffTree(self, forest: list[list[int]]) -> int:
        count=0
        row=len(forest)
        col=len(forest[0])
        result=[]
        for i in range(row):
            temp=0
            for j in range(col):
                if forest[i][j]!=0:
                    temp+=1
            result.append(temp) 
            
        return count-1
class TestApp:
      def testing_case_one(self):
          assert Solution().cutOffTree([[1,2,3],[0,0,4],[7,6,5]])==6
      def testing_case_two(self):
          assert Solution().cutOffTree([[1,2,3],[0,0,0],[7,6,5]])==-1
      def testing_case_three(self):
          assert Solution().cutOffTree([[2,3,4],[0,0,5],[8,7,6]])==6