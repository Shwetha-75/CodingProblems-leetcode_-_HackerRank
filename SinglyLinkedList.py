class Node:
    def __init__(self,val=0,next=None):
        self.value=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def addAtHead(self,value):
        node=Node()
        node.value=value
        if self.head==None:
            self.head=node
            
        else: 
            node.next=self.head
            self.head=node
        return "Inserted"
    def addAtTail(self,value):
        node=Node()
        node.value=value
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node 
            self.tail=node
        return "Inserted"
    def deleteAtHead(self):
        if self.head==None:
            return "No elements area there to delete"
        if self.head:
            temp=self.head.next
            self.head=temp
            return f"Deleted Element {temp.value}"
    def printing(self,root:Node):
        temp=root
        while temp!=None:
            print(temp.value,end=" ")
            temp=temp.next 
        
def main():
    ll=LinkedList()
    print(ll.addAtHead(30))    
    print(ll.addAtTail(40))
    ll.printing()
if __name__=="__main__":
    main()
    

        