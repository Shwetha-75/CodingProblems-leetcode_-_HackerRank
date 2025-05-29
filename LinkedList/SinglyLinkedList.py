class Node:
     def __init__(self,val):
         self.val=val 
         self.next=None 


class SinglyLinkedList:
        def __init__(self):
            self.head=None 
            self.tail=None 
     
        def insertAtHead(self,val:int=0):
            node=Node(val)
            if not self.head and not self.tail:
                self.head=node 
                self.tail=node 
                return self 
            node.next=self.head 
            self.head=node 
        def insertAtTail(self,val:int=0):
            node=Node(val)
            if not self.head and not self.tail:
                self.head=node 
                self.tail=node 
                return self 
            if self.tail.next==None:
                self.tail.next=node 
                self.tail=node
                return self 
        def removeHead(self):
            if not self.head and not self.tail:
                return None 
            if self.head.next==None:
               self.head=None 
               self.tail=None 
               return self 
            temp=self.head.next 
            self.head=temp
            return self 
        def removeTail(self):
            if not self.head and not self.tail:
                return None 
            if self.head==self.tail:
                self.head=None
                self.tail=None 
                return self 
            temp=self.head 
            while temp.next.next:
                  temp=temp.next 
            temp.next=None 
            self.tail=temp 
            return self 
        def display(self):
            temp=self.head
            while temp:
                  print(temp.val,end='->')
                  temp=temp.next 
            print('null',end='')
            print()
        def convertToList(self,temp=None):
            array=[]
            if not self.head: return array
            while temp:
                  array.append(temp.val)
                  temp=temp.next 
            return array 
                  
def main():
    node=SinglyLinkedList()
    node.insertAtTail(1)
    node.insertAtTail(2)
    node.insertAtTail(3)
    node.insertAtTail(4)
    node.display()
    node.insertAtHead(10)
    node.insertAtHead(12)
    node.insertAtHead(14)
    node.insertAtHead(16)
    node.display()
    node.removeHead()
    node.display()
    node.removeTail()
    node.removeTail()
    node.removeTail()
    node.removeTail()
    node.removeTail()
    
    node.removeTail()
    node.display()
main()

             
             
            
            