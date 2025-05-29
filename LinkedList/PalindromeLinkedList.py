from SinglyLinkedList import * 

class Solution:
      def checkPalindrome(self,head:Node)->bool:
            fast=slow=head 
            stack=[]
            while fast and fast.next:
                  stack.append(slow.val)
                  slow=slow.next 
                  fast=fast.next.next 
            if fast:
               slow=slow.next 
            while slow:
                  if stack.pop(-1)!=slow.val:
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
          assert Solution().checkPalindrome(node.head)==True 
      def testing_case_two(self):
          node=SinglyLinkedList()
          node.insertAtTail(1)
          node.insertAtTail(2)
          node.insertAtTail(2)
          assert Solution().checkPalindrome(node.head)==False