# Using one linked list 
class Node:
      def __init__(self,val:int=0):
          self.val=val 
          self.next=None 
          
class Queue:
        def __init__(self):
            self.head=None
            self.tail=None 
        def enqueue(self,val:int):
            node=Node(val)
            if not self.head:
               self.head=self.tail=node 
               return 
            self.tail.next=node 
            self.tail=node
            return 
        def dequeueAny(self):
            if not self.head :
                return -1 
            if not self.head.next:
               val=self.head.val 
               self.head=self.tail=None 
               return val 
            val=self.head.val 
            temp=self.head.next 
            self.head.next=None 
            self.head=temp 
            return val 
        def dequeueCat(self):
            if not self.head:
               return -1 
            if not self.head.next:
                if self.head.val == 0:
                   self.head=self.tail=None 
                   return 0 
                return -1 
            if self.head.val==0:
               temp=self.head.next 
               self.head.next=None 
               self.head=temp 
               return 1
            prev=None 
            curr=self.head 
            while curr:
                  next=curr.next 
                  if curr.val==0:
                     prev.next=next 
                     curr.next=None 
                     return 0 
                  prev=curr 
                  curr=next 
            return -1 
        def dequeueDog(self):
            if not self.head:
               return -1 
            if not self.head.next:
                if self.head.val == 1:
                   self.head=self.tail=None 
                   return 0 
                return -1 
            # check if t is present in the first node 
            if self.head.val==1:
               temp=self.head.next 
               self.head.next=None 
               self.head=temp 
               return 1
            prev=None 
            curr=self.head 
            while curr:
                  next=curr.next 
                  if curr.val==1:
                     prev.next=next 
                     curr.next=None 
                     return 1 
                  prev=curr 
                  curr=next 
            return -1
        def display(self):
            temp=self.head 
            while temp:
                  print(temp.val,end=" ")
                  temp=temp.next 
            print()

queue=Queue()
queue.enqueue(1) 
queue.enqueue(1) 
queue.enqueue(0) 
queue.enqueue(1) 
queue.enqueue(0) 
queue.enqueue(0) 
queue.display()
queue.dequeueDog()
queue.dequeueDog()
queue.display()