from SinglyLinkedList import *
class Solution:
      def nThElement(self,head:Node,n:int)->int:
            length=0 
            temp=head 
            while temp:
                  temp=temp.next 
                  length+=1 
            pos=length-n+1 
            if pos==1: return head.val
            length=0  
            while head:
                  length+=1 
                  if length==pos:
                     return head.val 
                 
                  head=head.next 
            return -1 


class TestApp:
        def testing_case_one(self):
            node=SinglyLinkedList()
            node.insertAtTail(1)
            node.insertAtTail(2)
            node.insertAtTail(3)
            node.insertAtTail(4)
            node.insertAtTail(5)
            assert Solution().nThElement(node.head,2)==4
        def testing_case_two(self):
            node=SinglyLinkedList()
            node.insertAtTail(1)
            node.insertAtTail(2)
            node.insertAtTail(3)
            node.insertAtTail(4)
            node.insertAtTail(5)
            assert Solution().nThElement(node.head,3)==3
        def testing_case_(self):
            node=SinglyLinkedList()
            node.insertAtTail(1)
            assert Solution().nThElement(node.head,1)==1
        def testing_case_four(self):
            node=SinglyLinkedList()
            node.insertAtTail(1)
            node.insertAtTail(2)
            node.insertAtTail(3)
            node.insertAtTail(4)
            node.insertAtTail(5)
            assert Solution().nThElement(node.head,1)==5