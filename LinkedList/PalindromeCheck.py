from SinglyLinkedList import *
class Solution:
        def isPalindrome(self, head:Node ) -> bool:
            array=[]
            temp=head 
            while temp:
                array.append(temp.val)
                temp=temp.next 
            return array==array[::-1]
# reversing the linked list 
class Solution:
        def isPalindrome(self, head:Node ) -> bool:
            node=SinglyLinkedList()
            temp=head 
            while temp:
                  node.insertAtHead(temp.val)
                  temp=temp.next 
                  
            head2=node.head
            while head and head2:
                  if head.val!=head2.val:
                     return False 
                  head=head.next 
                  head2=head2.next 
            return True 
# using stack data structure 
class Solution:
      def isPalindrome(self, head:Node ) -> bool:
            if not head or not head.next: return True 
            stack=[]
            slow=fast=head 
            while fast and fast.next:
                  stack.append(slow.val)
                  slow=slow.next 
                  fast=fast.next.next 
            if fast:
                slow=slow.next 
            while slow:
                  if slow.val != stack.pop(-1):
                     return False 
                  slow=slow.next 
            return True   

class TestApp:
    
      def testing_case_one(self):
          node=SinglyLinkedList()
          node.insertAtTail(1)
          node.insertAtTail(2)
          node.insertAtTail(2)
          node.insertAtTail(1)
          assert Solution().isPalindrome(node.head)==True 
      def testing_case_two(self):
          node=SinglyLinkedList()
          node.insertAtTail(1)
          node.insertAtTail(2)
          node.insertAtTail(2)
          assert Solution().isPalindrome(node.head)==False