#Problem Remove all the node in the linked list which is matching withe given value
class Node:
    def __init__(self,value):
        self.value=value 
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None 
        self.tail=None 
    def addAtTail(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node 
            self.tail=node
        else:
            node.prev=self.tail
            self.tail.next=node 
            self.tail=node 
    def printing(self):
        temp=self.head 
        while temp:
            print(temp.value,end=" ")
            temp=temp.next 
    def remove(self,node):
        if self.head==node:
            self.head=node.next 
        if self.tail==node:
            self.tail=node.prev
        #     1->2->3->4->null  value to be removed is 2
        #       node is 2 
        #     node need to iterate beacuse its double linked dlist
        #     if node.prev field exists 
        #         then node.prev.next field i.e, 1 should point to node.next 3
        #         then node.next field exists 3 should point 1
        #         1->3->4->null
        #
        if node.prev: 
            node.prev.next=node.next 
        if node.next:
            node.next.prev=node.prev 
        node.next=None 
        node.prev=None
    #Approach 1
    # def removeAllValueNode(self,value):
        
    #     if self.head.value==value:
    #         t1=self.head 
    #         self.head=t1.next 
    #         self.head.prev=None 
    #         t1.next=None
    #     if self.tail.value==value:
    #         t2=self.tail 
    #         self.tail=t2.prev 
    #         self.tail.next=None 
    #         t2.prev=None 
    #     temp1=self.head 
    #     count=0
    #     while temp1:
    #         count+=1
    #         temp1=temp1.next 
    #     count2=0
    #     temp1=self.head 
    #     while temp1:
    #         if temp1.value==value:
    #             count2+=1 
    #         temp1=temp1.next 
    #     if count==count2:
    #         self.head=None 
    #         self.tail=None 
    #         return 
    #     print(count,count2)
    #     temp=self.head   
    #     while temp:
    #         if temp.value==value:
    #             temp1=temp.prev 
    #             temp2=temp.next 
    #             temp1.next=temp2
    #             temp2.prev=temp1 
    #             temp=temp2 
    #         else:
    #             temp=temp.next
    
    #Observations 
    #1. If the all the nodes have the same value remove all the nodes 
    #2. If none of the nodes have the value 
    #3. If the value is at head or tail
    #4. If the linked list is empty 
    #   I didn't made a note and the previous will not work for few teste cases above
    def allRemoveMethod(self,value):
        #create current ptr 
        cur=self.head 
        #iterate until cur exists
        while cur:
            temp=cur 
            
            cur=cur.next 
            if temp.value==value:
                self.remove(temp)
            
            
def main():
    double=DoublyLinkedList()
    # double.addAtTail(30)
    # double.addAtTail(20)
    # double.addAtTail(20)
    # double.addAtTail(40)
    # double.addAtTail(20)
    # double.addAtTail(30)
    double.printing()
    double.allRemoveMethod(40)
    print()
    double.printing()
main()