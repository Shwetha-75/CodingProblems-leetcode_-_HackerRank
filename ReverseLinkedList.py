class Node:
    def __init__(self,value):
        self.value=value
        self.next=None 
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None 
    def addAtTail(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node 
            self.tail=node
        else:
            self.tail.next=node 
            self.tail=node 
    def printing(self):
         temp=self.head
         while temp:
             print(temp.value,end=' ')
             temp=temp.next 
    def reverse(self,left,right):
        def previousNode(node):
            temp=self.head 
            while temp.next:
                if temp.next.value==node.value:
                    return temp 
                temp=temp.next 
        def findNode(number):
            count=1
            temp=self.head
            while temp:
                temp=temp.next 
                count+=1
                if count==number:
                    return temp 
        left=findNode(left)
        #print(left.value)
        right=findNode(right)
        #print(right.value)
        print()
        while left.next and right:
              left.value,right.value=right.value,left.value 
              print(left.value,right.value)
              left=left.next 
              if left.next==right: break
              right=previousNode(right)
def main():
    ll=LinkedList()
    ll.addAtTail(1)
    ll.addAtTail(2)
    ll.addAtTail(3)
    ll.addAtTail(4)
    ll.addAtTail(5)
    ll.addAtTail(6)
    ll.addAtTail(7)
    ll.addAtTail(8)
    ll.addAtTail(9)
 
 
    ll.printing()
    ll.reverse(2,7)
    print()
    ll.printing()
main()