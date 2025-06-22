class Solution:
      def __init__(self):
          self.array=[]
      def find(self,node):
          if self.array[node]==node:
             return node 
          return self.find(self.array[node]) 
      def union(self,node_1,node_2):
          left=self.find(node_1)
          right=self.find(node_2)
          if left!=right:
              for i in range(len(self.array)):
                  if self.array[i]==left:
                     self.array[i]=right 
      def findCircleNum(self, isConnected: list[list[int]]) -> int:
          n=len(isConnected)
          self.array=list(range(n))
          m=len(isConnected[0])
          for i in range(n):
              for j in range(m):
                  if isConnected[i][j]==1 and i!=j:
                      self.union(i,j)
          return len(set(self.array))
class TestApp:
      def testing_case_one(self):
          assert Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])==2 
      def testing_case_two(self):
          assert Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]])==3 
    
    