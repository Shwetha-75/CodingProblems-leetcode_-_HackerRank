from SinglyLinkedList import *
class Solution:
      def removeNthFromEnd(self, head:Node, n: int) -> Node:
            if not head or n==0: return head 
            length=0 
            temp=head
            while temp:
                  temp=temp.next 
                  length+=1 
            pos=length-n+1 
            if pos==1:
               if not head.next:
                     head=None 
                     return None 
               return head.next
            temp=head 
            prev=None
            length=0
            curr=head
            while curr:
                  length+=1 
                  next=curr.next
                  if length==pos:
                     prev.next=curr.next 
                     curr.next=None 
                     return head 
                  prev=curr
                  curr=next 
                  
            return head   
        
class TestApp:
        def testing_case_one(self):
            node=SinglyLinkedList()
            node.insertAtTail(1)
            node.insertAtTail(2)
            node.insertAtTail(3)
            node.insertAtTail(4)
            node.insertAtTail(5)
            assert node.convertToList(Solution().removeNthFromEnd(node.head,2))==[1,2,3,5]
        def testing_case_two(self):
            node=SinglyLinkedList()
            node.insertAtTail(1)
            node.insertAtTail(2)
            node.insertAtTail(3)
            node.insertAtTail(4)
            node.insertAtTail(5) 
            assert node.convertToList(Solution().removeNthFromEnd(node.head,3))==[1,2,4,5]
        def testing_case_(self):
            node=SinglyLinkedList()
            node.insertAtTail(1)
            assert node.convertToList(Solution().removeNthFromEnd(node.head,1))==[]
        def testing_case_four(self):
            node=SinglyLinkedList()
            node.insertAtTail(1)
            node.insertAtTail(2)
            node.insertAtTail(3)
            node.insertAtTail(4)
            node.insertAtTail(5)
            assert node.convertToList(Solution().removeNthFromEnd(node.head,1))==[1,2,3,4]