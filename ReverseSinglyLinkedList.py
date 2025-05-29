class Node :
    def __init__(self,value):
        self.value=value
        self.next=None

class SingleLinkedList:
    def __init__(self,head):
        self.head=head
        self.head2=None
    def reverseSinglyLinkedList(self):
        temp=self.head
        
        while temp!=None:
        
            node=Node(temp.value)
            if self.head2==None:
                self.head2=node 
            else:
                node.next=self.head2
                self.head2=node 
            temp=temp.next 
        self.head=self.head2
        
    def printing(self):
        vari=self.head2 
        
        while vari!=None:
              print(vari.value,end=" ")
              vari=vari.next

def main():
    
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    single=SingleLinkedList(head)
    single.reverseSinglyLinkedList()
    single.printing()
main()