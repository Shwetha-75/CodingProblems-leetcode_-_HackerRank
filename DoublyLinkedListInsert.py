class Node:
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def addTail(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node 
            
            self.tail=node 
        else:
            node.prev=self.tail
            self.tail.next=node 
            
            self.tail=node 
    def removalNode(self,node):
        if node.value==self.head.value: 
            head=self.head
            self.head=head.next 
            self.head.prev=None
            head.next=None
        if node.value==self.tail:
            tail=self.tail
            self.tail=tail.prev 
            tail.prev=None 
            self.tail.next=None
        temp=self.head 
        while temp:
            if temp.value==node.value:
               temp1=temp.prev
               temp2=temp.next 
               temp1.next=temp2
               temp2.prev=temp1 
               break 
            temp=temp.next
        return self.head
    def insertion(self,node1,node2):
        if node1==None:
            self.addTail(node2.value)
            return 
        if self.head.value==node1.value:
            self.head.prev=node2
            node2.next=self.head 
            self.head=node2
            return 
       
        self.removalNode(node2)
        temp=self.head
        while temp:
            if temp.value==node1.value:
               temp1=temp.prev 
               temp2=temp1.next 
               node2.prev=temp1
               node2.next=temp2
               temp1.next=node2
               temp2.prev=node2
            temp=temp.next 
        
    def printing(self):
        temp=self.head
        while temp:
            print(temp.value,end=' ')
            temp=temp.next
        print()
    
def main():
    double=DoublyLinkedList()
    node1=Node(1)
    node2=Node(5)
    double.addTail(1)
    double.addTail(2)
    double.addTail(3)
    double.addTail(4)
    double.printing()
    #double.removalNode(node1)
    double.insertion(node1,node2)
    double.printing()
main()
    