class Solution:
    def __init__(self):
        self.array=[]
    def find(self,value):
        if self.array[value]==value:
            return value 
        return self.find(self.array[value])
    def union(self,value_1,value_2):
        left=self.find(value_1)
        right=self.find(value_2)
        if left!=right:
           for i in range(len(self.array)):
               if self.array[i]==left:
                   self.array[i]=right  
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        self.array=list(range(len(isConnected)))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1 and i!=j:
                   self.union(i,j)
                  
        return len(set(self.array))
class TestApp:
      def testing_case_one(self):
          assert Solution().findCircleNum([[1, 1, 0, 0, 0],[1, 1, 0, 1, 1],[0, 0, 1, 0, 0],[0, 1, 0, 1, 0],[0, 1, 0, 0, 1]])==2
      def testing_case_two(self):
          assert Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]])==3
      def testing_case_three(self):
          assert Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])==2
      def testing_case_four(self):
          assert Solution().findCircleNum([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])==4          
                    