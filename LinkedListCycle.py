#Hash map 
#Linked List Cycle detection using brut force approach

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None 
def cycleDetection(head):
    dict1={}
    temp=head 
    #trvaersing through linked list
    while temp:
        #checking the address
        if temp in dict1:
            return temp 
        else:
            #storing the linked list address if not found
            dict1[temp]=True
        #changing the address 
        temp=temp.next
def main():
    node=Node(1)
    node.next=Node(2)
    node.next.next=Node(3)
    node.next.next.next=Node(4)
    node.next.next.next.next=Node(5)
    node.next.next.next.next.next=Node(6)
    node.next.next.next.next.next.next=Node(7)
    node.next.next.next.next.next.next.next=Node(8)
    node.next.next.next.next.next.next.next.next=Node(9)
    node.next.next.next.next.next.next.next.next.next=node.next.next
    print(cycleDetection(node).value)
main()
    
    
           