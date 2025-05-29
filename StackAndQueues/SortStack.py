class SortStack:
        def __init__(self):
            self.stack=[]
            self.temp=[]
        def push(self,val:int)->None:
            if not self.stack:
               self.stack.append(val)
               return 
            if self.stack[-1]<val:
               while self.stack:
                     self.temp.append(self.stack.pop(-1))
               self.stack.append(val)
               while self.temp:
                   self.stack.append(self.temp.pop(-1))
               return 
            self.stack.append(val)
        def pop(self):
            if len(self.stack)==1 or len(self.stack)==2:
               val=self.stack.pop(-1)
               return val 
            if self.stack:
                val=self.stack.pop(-1)
                min_elem=self.stack.pop(-1)
                while self.stack:
                      cur=self.stack.pop(-1)
                      if min_elem>cur:
                          self.temp.append(min_elem)
                          min_elem=cur 
                      else:
                          self.temp.append(cur)
                while self.temp:
                     self.stack.append(self.temp.pop(-1))
                self.stack+=[min_elem]
                return val 
            return -1
        def peek(self):
            return self.stack[-1] if self.stack else -1 
        def isEmpty(self):
            return not self.stack 
        def display(self):
            for ele in self.stack:
                print(ele,end=" ")
            print()
stack=SortStack()
stack.push(1)
stack.push(7)
stack.push(6)
stack.push(8)
stack.push(3)
stack.push(4)
stack.display()
print(stack.peek())
print(stack.pop())
stack.display()
print(stack.pop())
stack.display()
print(stack.pop())
stack.display()
stack.push(10)
stack.push(1)
stack.display()
stack.push(99)
stack.push(39)
stack.push(69)
stack.display()
print(stack.pop())
stack.display()
print(stack.pop())
stack.display()
print(stack.pop())
stack.display()
print(stack.pop())
stack.display()
print(stack.pop())
stack.display()
stack.display()
print(stack.pop())
stack.display()
