from SinglyLinkedList import Node
class Solution:
    
    def sortList(self, head:Node) ->Node:
        # Merge Sort 
        # Divide And Conquer Approach 
        return self.divide(head)
 
    def divide(self,head:Node)->Node:
        # using hare and tortoise Approach 
        
        left=head 
        right=self.findMid(head)
        temp=right.next
        right.next=None 
        right=temp 
        left=self.divide(left)
        right=self.divide(right)
        return self.merge(left,right)
    # Finding the mid node 
    def findMid(self,head:Node)->Node:
        slow=head 
        fast=head.next 
        while fast and fast.next:
              slow=slow.next 
              fast=fast.next.next 
        return slow
    # Merging the node 
    def merge(self,list1:Node,list2:Node):
        dummy=tail=Node(0)
        while list1 and list2:
              if list1.val<list2.val:
                  tail.next=list1
                  list1=list1.next
              else:
                  
                  tail.next=list2
                  list2=list2.next 
              tail=tail.next 
        tail.next=list1 if list1 else list2 
        return dummy.next   
        