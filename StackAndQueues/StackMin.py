class Solution:
      def __init__(self):
          self.stack=[]
      def push(self,val):
          temp_min_val=self.getMin()
          if temp_min_val==None or temp_min_val>val:
             temp_min_val=val 
          self.stack.append([val,temp_min_val])
      def pop(self):
          return self.stack.pop[0] if self.stack else None 
      def top(self):
          return self.stack[-1][0] if self.stack else None
      def getMin(self): 
          return self.stack[-1][1] if self.stack else None 