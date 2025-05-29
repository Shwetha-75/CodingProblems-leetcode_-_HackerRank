class Node:
      def __init__(self,val=0):
          self.val=val
          self.next=None
           
class Queue:
        def __init__(self):
            self.head=None 
            self.tail=None 
        def add(self,val:int=0):
            node=Node(val)
            if not self.head and not self.tail:
               self.head=self.tail=node 
               return self
            
            self.tail.next=node 
            self.tail=node 
            return self 
        def remove(self):
            if not self.head and not self.tail:
               return None 
            if not self.head.next:
               val=self.head.val 
               self.head=self.tail=None 
               return val 
            val=self.head.val 
            self.head= self.head.next 
            return val 
        def peek(self):
            if not self.head and not self.tail:
               return None 
            
            return self.head.val 
            
        def isEmpty(self):
            return self.head==None 
        def display(self):
            temp=self.head
            while temp:
                  print(temp.val,end=" ") 
                  temp=temp.next 
            print()
            

queue=Queue()
queue.add(10)
queue.add(20)
queue.add(30)
queue.display()
print(queue.peek())
queue.remove()
queue.remove()
queue.remove()
queue.display()