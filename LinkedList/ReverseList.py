from SinglyLinkedList import * 
class Solution:
      def reverseThLinkedList(self,head:Node)->Node:
          prev=None 
          curr=head 
          while curr:
                next=curr.next 
                curr.next=prev 
                prev=curr 
                curr=next 
          return prev 
class TestApp:
      def testing_case_two(self):
          node=SinglyLinkedList()
          node.insertAtTail(1)
          node.insertAtTail(2)
          node.insertAtTail(3)
          node.insertAtTail(4)
          node.insertAtTail(5)
          node.insertAtTail(6)
          result=Solution().reverseThLinkedList(node.head)
          assert node.convertToList(result)==[6,5,4,3,2,1]
      def testing_case_three(self):
          node=SinglyLinkedList()
          node.insertAtTail(1)
          node.insertAtTail(2)
          node.insertAtTail(3)
          result=Solution().reverseThLinkedList(node.head)
          assert node.convertToList(result)==[3,2,1]
          