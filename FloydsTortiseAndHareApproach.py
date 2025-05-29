#Using Floyd/'s Tortise and Hare approach we are going to detect the linked list cycle
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None 
    pass 
def cycleDetection(head):
    #Observations 
    #there is no linked list
    if not head: return None
    #if there only one linked list node
    if not head.next:  return None 
    #tortoise
    #hare
    tortoise=head
    hare=head
    #First mistake was i have took the 
    #stopping condition was tortoise!=hare --->this approach will not work
    while hare and hare.next :
        tortoise=tortoise.next #tortoise moves one step
        hare=hare.next.next#hare moves two stpes a head
        if tortoise==hare:
            break
        
    #if the given linked list is not having cycle 
    if tortoise!=hare:#because hare will be pointing towards None 
        return None
    #we have to find from wher the cycle getting started and we have to return that node
    ptr=head 
    while ptr!=tortoise:
        ptr=ptr.next 
        tortoise=tortoise.next 
    return ptr
    
    pass
def main():
    
    node=Node(1)#                            1-->2-->3-->4-->5-->6-->7-->8-->9
    node.next=Node(2)#                               |                       |
    node.next.next=Node(3)#                          -------------------------                   
    node.next.next.next=Node(4)#
    node.next.next.next.next=Node(5)#
    node.next.next.next.next.next=Node(6)#
    node.next.next.next.next.next.next=Node(7)#
    node.next.next.next.next.next.next.next=Node(8)#
    node.next.next.next.next.next.next.next.next=Node(9)#
    node.next.next.next.next.next.next.next.next.next=node.next.next#
    print(cycleDetection(node).value)
main()
    
    
            