class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        

    
    
node=Node(1)
node.next=Node(2)
node.next.next=Node(3)
node.next.next.next=Node('a')


def remove(node):
    #we are storing the node value in temp variable
    temp=node
    #looping until temp!=None
    while temp:
        #nextVlaue can hold address of next pointer     temp  nextValue
        nextValue=temp.next#                               |  |
        #first nextVlaue should not be null 1->1->2->2->2->3->3->null
        while nextValue!=None and temp.value==nextValue.value :
            nextValue=nextValue.next#keep on updating if you found same value
        temp.next=nextValue#if the value is distinct temp.next field will be having address of distinct value
        temp=nextValue#we should update temp to point nextValue
    return node #1->2->2->2->3->null
#                   |        |
#                   temp     nextValue  
#                    temp.next=nextValue
#                             |  temp=nextValue
#                             temp
def printValue(node):
    temp=node 
    
    while temp!=None:
        print(temp.value,end=" ")
        temp=temp.next 
node=remove(node)
printValue(node)
