import heapq
class DinnerPlates:
        def __init__(self,capacity):
            self.stack=[]
            self.temp=[]
            self.capacity=capacity
        def push(self,val:int):
            if self.temp:
               index=heapq.heappop(self.temp)
               if index<len(self.stack):
                  self.stack[index]+=[val]
                  return 
               else:
                   self.temp=[]
            if self.stack and len(self.stack[-1])<self.capacity:
               self.stack[-1]+=[val]
               return 
            self.stack+=[[val]]
        def pop(self):
            while self.stack and not self.stack[-1]:
                  self.stack.pop()
            if self.stack:
               val=self.stack[-1][-1]
               self.stack[-1].pop(-1)
               return val 
            return -1 
        def popAtStack(self,index:int):
            if index<len(self.stack) and self.stack[index]:
               val=self.stack[index][-1]
               heapq.heappush(self.temp,index)
               self.stack[index].pop(-1)
               return val 
            return -1 
        
               