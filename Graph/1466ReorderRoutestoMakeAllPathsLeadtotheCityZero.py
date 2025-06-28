class Solution: 
      def __init__(self):
          self.count=0
          self.directed_graph={}
          self.undirected_graph={}
          self.visited=set()
      def minReorder(self, n: int, connections: list[list[int]]) -> int:
          for i in range(n):
              self.directed_graph[i]=set()
              self.undirected_graph[i]=[] 
          for connection in connections:
              node_1,node_2=connection[0],connection[1]
              self.undirected_graph[node_1].append(node_2)
              self.undirected_graph[node_2].append(node_1)
              self.directed_graph[node_1].add(node_2)
          self.helper(0)    
          return self.count

      def helper(self,node):
         
          self.visited.add(node)
          for value in self.undirected_graph[node]:
              if value in self.visited:
                 continue
              if node not in self.directed_graph[value]:
                 self.count+=1
              self.helper(value)
          return  
          
          
          
            
class TestApp:
      def testing_case_one(self):
          assert Solution().minReorder(6,[[0,1],[1,3],[2,3],[4,0],[4,5]])==3 
      def testing_case_two(self):
            assert Solution().minReorder(5,[[1,0],[1,2],[3,2],[3,4]])==2
      def testing_case_three(self):
            assert Solution().minReorder(3,[[1,0],[2,0]])==0     