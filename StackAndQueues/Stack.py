# using Linked list \
class Node:
      def __init__(self,val:int=0):
          self.val=val 
          self.next=None 
          
class Stack:
      def __init__(self):
          self.head=None 
          self.tail=None 
      def push(self,val=0):
          node=Node(val)
          if not self.head:
             self.head=node 
             self.tail=node 
             return self 
          self.tail.next=node 
          self.tail=node 
          return self 
      def pop(self):
          if not self.head and not self.tail:
             return None 
          if not self.head.next:
             val=self.tail.val
             self.head=None
             self.tail=None 
             return val 
          temp=self.head 
          while temp.next.next:
               temp=temp.next 
          val=temp.next.val
          temp.next=None 
          self.tail=temp 
          return val 
      def peek(self):
          if not self.head and not self.tail:
             return None 
          if not self.head.next:
             return self.tail.val 
            
          temp=self.head 
          while temp.next.next:
               temp=temp.next 
          return temp.next.val
      def isEmpty(self):
          return self.head==None 
      def display(self):
          temp=self.head 
          while temp:
                print(temp.val,end=" ")
                temp=temp.next 
          print()    
       
stack= Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.display()
print(stack.peek())
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.display()
print(stack.isEmpty())