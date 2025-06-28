class Queue:
      def __init__(self):
          self.stack_push=[]
          self.stack_pop=[]
      def push(self,val:int):
          self.stack_push+=[val]
      def pop(self):
          if self.stack_pop:
             return self.stack_pop.pop(-1)
          if self.stack_push:
             while self.stack_push:
                   self.stack_pop+=[self.stack_push.pop(-1)]
             return self.stack_pop.pop(-1)
          return -1 
      def peek(self):
          if self.stack_pop:
              return self.stack_pop[-1]
          if self.stack_push:
              return self.stack_push[0]
          return -1 
      def isEmpty(self):
          return True if not self.stack_push and not self.stack_pop else False 
      def display(self):
          for element in self.stack_pop:
              print(element,end=" ")
          for element in self.stack_push:
              print(element,end=" ")
          print()
          
queue=Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)
queue.display()
print(queue.peek())
queue.pop()
queue.pop()
queue.pop()
queue.pop()
queue.display()
