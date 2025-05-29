from SinglyLinkedList import * 
class Solution:
      def detectLoop(self,head:Node)->bool:
            hare=tortoise=head 
            while hare and hare.next:
                  hare=hare.next.next 
                  tortoise=tortoise.next 
                  if hare==tortoise:
                     return True 
            return False 

class TestApp:
      def testing_case_one(self):
          node=SinglyLinkedList()
          node.insertAtTail(1)
          node.insertAtTail(2)
          node.insertAtTail(3)
          node.insertAtTail(4)
          node.insertAtTail(5)
          node.tail.next=node.head.next.next
          assert Solution().detectLoop(node.head)==True 
      def testing_case_two(self):
          node=SinglyLinkedList()
          node.insertAtTail(1)
          node.insertAtTail(2)
          node.insertAtTail(3)
          node.insertAtTail(4)
          node.insertAtTail(5)
          assert Solution().detectLoop(node.head)==False 
      def testing_case_three(self):
          node=SinglyLinkedList()
          node.insertAtTail(1)
          node.insertAtTail(2)
          node.tail.next=node.head 
          assert Solution().detectLoop(node.head)==True 
          