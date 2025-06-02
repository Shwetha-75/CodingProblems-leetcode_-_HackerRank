import heapq
class Solution:
      def __init__(self,k:int,nums:list[int]):
          self.k=k 
          self.nums=nums 
          self.heap=[]
          for num in self.nums:
              heapq.heappush(self.heap,num)
      def remove(self,val:int):
          heapq.heappush(self.heap,val)
          while len(self.heap)>self.k:
                heapq.heappop(self.heap)
          return self.heap[0]

class TestApp:
      def testing_case_one(self):
          sol=Solution(3,[4,5,8,2])
          arr=[3,5,10,9,4]
          ans=[4,5,5,8,8]
          index=0
          for element in arr:
              assert sol.remove(element)==ans[index]
              index+=1
         