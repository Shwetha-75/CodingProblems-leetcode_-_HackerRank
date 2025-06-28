import heapq
class Stack:
    def __init__(self,capacity):
        self.capacity=capacity
        self.stack:list[list[int]]=[]
        self.trackIndex=[]
    def push(self,val:int):
        #   check if the val has to be inserted at middle stack in collection of stack 
        if self.trackIndex:
            index=heapq.heappop(self.trackIndex)
            if index < len(self.stack):
                self.stack[index]+=[val]
                return 
            else:
                self.trackIndex=[]
        if len(self.stack)>0 and len(self.stack[-1])<self.capacity:
           self.stack[-1]+=[val]
           return 
        self.stack+=[[val]]
    def pop(self):
        while self.stack and not self.stack[-1]:
              self.stack[-1].pop()           
        if self.stack:
           val=self.stack[-1][-1]
           self.stack[-1].pop(-1)
           return val 
        return -1 
    def popAtIndex(self,index:int):
        if index < len(self.stack) and len(self.stack[index])>0:
            val=self.stack[index][-1]
            self.stack[index].pop(-1)
            return val 
        return -1 