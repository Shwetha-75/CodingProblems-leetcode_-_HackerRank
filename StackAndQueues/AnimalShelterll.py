class Node:
    def __init__(self,val:int):
        self.val=val 
        self.next=None 

class Queue:
        def __init__(self):
            self.head0=None 
            self.tail0=None 
            self.head1=None 
            self.tail1=None 
            self.random=0
        def enqueue(self,val:int):
            node=Node(val)
            
            if val==0:
                if not self.head0:
                   self.head0=self.tail0=node 
                   return  self
                self.tail0.next=node 
                self.tail0=node 
                return self
            else:
                if not self.head1:
                   self.head1=self.tail1=node 
                   return 
                self.tail1.next=node 
                self.tail1=node 
                return self
        def dequeueAny(self):
            if not self.head0 and self.head1:
                return -1 
            if self.random==0:
                if self.head0:
                    if not self.head0.next:
                       self.head0=self.tail0=None 
                    else:
                        temp=self.head0.next 
                        self.head0.next=None 
                        self.head0=temp 
                    self.random=1 
                    return 0 
                elif self.head1:
                    if not self.head1.next:
                       self.head1=self.tail1=None 
                    else:
                        temp=self.head1.next 
                        self.head1.next=None 
                        self.head1=temp 
                    self.random=0 
                    return 1
            else:
                if self.head1:
                    if not self.head1.next:
                       self.head1=self.tail1=None 
                    else:
                        temp=self.head1.next 
                        self.head1.next=None 
                        self.head1=temp 
                    self.random=0 
                    return 1 
                elif self.head0:
                    if not self.head0.next:
                       self.head0=self.tail0=None 
                    else:
                        temp=self.head0.next 
                        self.head0.next=None 
                        self.head0=temp 
                    self.random=1 
                    return 0   
            return -1 
        def dequeueCat(self):
            if not self.head0:
               return -1 
            if not self.head0.next:
               self.head0=self.tail0=None 
               return 0 
            temp=self.head0.next 
            self.head0.next=None 
            self.head0=temp 
            return 0 
        def dequeueDog(self):
            if not self.head1:
                return -1 
            if not self.head1.next:
               self.head1=self.tail1=None 
               return 1 
            temp=self.head1.next 
            self.head1.next=None 
            self.head1=temp 
            return 1  
        def displayCat(self):
            temp=self.head0
            while temp:
                  print(temp.val,end=" ")
                  temp=temp.next 
            print() 
            return self
        def displayDog(self):
            temp=self.head1
            while temp:
                  print(temp.val,end=" ")
                  temp=temp.next 
            print() 
            return self
                   
queue=Queue()
queue.enqueue(0)
queue.enqueue(0)
queue.enqueue(0)
queue.enqueue(1)
queue.enqueue(1)
queue.enqueue(1)
queue.enqueue(1)
queue.displayCat()
queue.dequeueAny()
queue.displayDog()
queue.dequeueAny()
queue.dequeueAny()
queue.displayDog()
queue.displayCat()
queue.dequeueCat()
queue.displayCat()
queue.dequeueDog()
queue.dequeueDog()
queue.displayDog()