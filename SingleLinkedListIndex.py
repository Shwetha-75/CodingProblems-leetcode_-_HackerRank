#Node class with two fields val and next 
class Node:
    def __init__(self,val): 
        self.val=val
        self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=None#head
        self.tail=None#tail
        self.size=0#size to get the index
        
    #get method to get the node at specified index
    def get(self,index):
        #observations
        if index<0 or index>=self.size:
            return -1
        counter=0
        temp=self.head
        while counter!=index:
            temp=temp.next 
            counter+=1
        return temp#return the node
    def addHead(self,value):
        node=Node(value)
        if not self.head:#if it is the first element
            self.head=node
            self.tail=node
        else:
            temp=self.head#keep the head node in temp
            self.head=node#assign head to new node
            node.next=temp #assign the  new node next to hold the temp node
        self.size+=1
        return self
    def addTail(self,value):
        node=Node(value)
        if not self.head:
            self.head=node
            self.tail=node
        else:
            
            self.tail.next=node
            self.tail=node
        self.size+=1
        return self
    def addIndex(self,index,value):
        node=Node(value)
        if index<0 or index > self.size: return "invalid index"
        if index==0:  return self.addHead(value)
        if index==self.size: return self.addTail(value)
        previous=self.get(index-1)# 1->2->3->null
        temp=previous.next#       4    |-->insertion at this position
        previous.next=node#            previous ==1   temp=2->3->null
        node.next=temp#                1->4->2->3->null
        self.size+=1
        return self
    def deleteIndex(self,index):
        #observations
        #in=f the index is ranging out of bounds return invalid index
        if index<0 or index> self.size:
            return "invalid index"
        #if it is 0th index
        if index==0:
            #store the self.head in temp var
            temp=self.head
            #point the eself.head to hold temp.next element
            self.head=temp.next
            ##decrement the size
            self.size-=1
            #if the size is zero
            if self.size==0:
                #point the tail to hold None 
                self.tail=None
            #return the value deleted
            return temp.val
        #if it is last index or last node
        if index==self.size:
            #store the tail in temp var
            oldTail=self.tail
            #get the previous indexed node
            previous=self.get(index-1)
            ##point the previous index node to none           self.tail
            previous.next=None                               #|
            ##the tail should point to previous node    1->2->3->null i want to delete 3 
            self.tail=previous#                         1->2->3->null                   
            self.size-=1#                                  |            1->2->null
            return oldTail.val #                          self.tail        |
                                                    #                    self.tail
        #deleted index is 1                   
        #1->2->->3->null
        previous=self.get(index-1) # prevoius=1        temp.next
        temp=previous.next#          temp=2->3->null    |
        previous.next=temp.next#     previous.next=> 1->3->-null
        self.size-=1#
        return temp.val#
    
        
    def print(self):
       
        if not self.head:
            print("Nothing is there to print")
        else:
             temp=self.head
             while temp!=None:
                 print(temp.val,end=" ")
                 temp=temp.next  
            
            
def main():
    single=SingleLinkedList()
    single.addHead(10)
    single.addTail(30)
    single.addTail(40)
    single.addIndex(1,66)
    print(single.deleteIndex(1))
    single.print()
main()