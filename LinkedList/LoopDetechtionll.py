from SinglyLinkedList import * 
class Solution:
      def detectTheCycle(self,head:Node)->Node:
        #   detect if the cycle exist or not 
        def hasCycle(head:Node)->Node:
            fast=slow=head
            while fast and fast.next:
                  fast=fast.next.next 
                  slow=slow.next
                  if slow==fast:
                     ptr=head 
                     while ptr!=slow:
                           ptr=ptr.next 
                           slow=slow.next 
                     return ptr 
            return None 
        return hasCycle(head) 
    
class TestApp:
      def testing_case_one(self):
          node=SinglyLinkedList()
          node.insertAtTail(1)
          node.insertAtTail(2)
          node.insertAtTail(3)
          node.insertAtTail(4)
          node.insertAtTail(5)
          node.tail.next=node.head.next.next
          assert Solution().detectTheCycle(node.head)==node.head.next.next
      def testing_case_two(self):
          node=SinglyLinkedList()
          node.insertAtTail(1)
          node.insertAtTail(2)
          node.insertAtTail(3)
          node.insertAtTail(4)
          node.insertAtTail(5)
          assert not Solution().detectTheCycle(node.head)
      def testing_case_three(self):
          node=SinglyLinkedList()
          node.insertAtTail(1)
          node.insertAtTail(2)
          node.tail.next=node.head 
          assert Solution().detectTheCycle(node.head)==node.head 