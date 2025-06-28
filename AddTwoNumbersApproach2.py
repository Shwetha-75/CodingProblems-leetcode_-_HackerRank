class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def addTwoNumbers(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
            self.tail=node 
        else:
            self.tail.next=node 
            self.tail=node 
        return self.head
def addTwoNumbers(list1,list2):
    #prequisites are carry varibale to carry the sum
    carry=0
    ll=LinkedList()
    root=None
    #iterating through until list1 have node 
    #or list2 have node or carry is not equal to zero
    while list1 or list2 or carry: 
            #carry=0   --->            0     0     1    1
            #1->5->7->null  --->       1     5     7    0(null)
            #2->6->7->null --->       +2    +6    +7    0(null)
            #      result   --->       3     11    15   1
            #creating node for value 3%10, carry is 3//10--> 0  
            #  3->null
            # | adding at tail by taking 11%10 1, carry 1//10-->1
            #   3->1->null
            #  for result 15%10-->5, carry is 15//10-->1
            #  3->1->5->1->null
            #
            #
            #
            #ternary check
            #checking if the linked list has node or not 
            #if not returning  0 or else returning value
            value1=list1.value if list1!=None else 0
            #if not returning  0 or else returning value
            value2=list2.value if list2!=None else 0
            #adding the values of linked list and carry
            #
            #adding result with carry
            result=value1+value2+carry
            #taking moduls of result (last digit)
            nodeValue=result%10
            #appending it to tail
            root=ll.addTwoNumbers(nodeValue)
            #dividing to reduce the digit
            carry=result//10
            #updating the lnked list
            list1=list1.next if list1!=None else None 
            list2=list2.next if list2!=None else None
    return root
def main():
    node1=Node(1)
    node1.next=Node(5)
    node1.next.next=Node(7)
    
    node2=Node(2)
    node2.next=Node(6)
    node2.next.next=Node(7)
    
    root=addTwoNumbers(node1,node2)
    
    while root:
        print(root.value,end="")
        root=root.next 
main()
    
            
            