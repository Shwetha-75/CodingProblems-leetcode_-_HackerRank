class Node:
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None 
        self.tail=None
        
    def insertionAtTail(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
            self.tail=node 
        else:
            temp=self.tail 
            self.tail.next=node 
            node.prev=temp 
            self.tail=node 
        return self.head
    def printing(self):
        temp=self.head 
        while temp:
            print(temp.value,end=' ')
            temp=temp.next 
    def removeNode(self,root):
        temp=self.head
        while temp:
            if temp.value==root.value:
                temp1=temp.prev 
                temp2=temp.next 
                temp1.next=temp2
                temp2.prev=temp1
                temp.prev=None 
                temp.next=None
                return f"Removed node: {temp.value}"
            temp=temp.next 
        return f"Node Does not exist {root.value}"
        pass
def main():
    dob=DoublyLinkedList()
    node=Node(89)
    dob.insertionAtTail(23)
    dob.insertionAtTail(45)
    dob.insertionAtTail(67)
    dob.insertionAtTail(89)
    dob.insertionAtTail(90)
    dob.insertionAtTail(13)
    dob.printing()
    print()
    print(dob.removeNode(node))

    dob.printing()
    
main()