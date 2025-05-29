from SinglyLinkedList import *
class Solution:
        def __init__(self):
            self.head=None
        def insertAtTail(self,val:int=0):
            node=Node(val)
            if not self.head and not self.tail:
                self.head=node 
                self.tail=node 
                return self 
            if self.tail.next==None:
                self.tail.next=node 
                self.tail=node
                return self
        def addTwoNumbers(self,l1:Node,l2:Node)->Node:
            if not l1 or not l2:
               return l1 if l1 else l2 
            carry=0
            total_sum=0 
            while l1 and l2:
                  total_sum=l1.val+l2.val+carry
                  
                  self.insertAtTail(total_sum%10)
                  carry=total_sum//10 
                  l1=l1.next 
                  l2=l2.next 
            while l1:
                  total_sum=l1.val+carry
                  self.insertAtTail(total_sum%10)
                 
                  carry=total_sum//10 
                  l1=l1.next 
            while l2:
                  total_sum=l2.val+carry
                  self.insertAtTail(total_sum%10)
                  carry=total_sum//10 
                  l2=l2.next 
            if carry!=0:
               self.insertAtTail(carry)      
            return self.head 

            
                   
                
              
            