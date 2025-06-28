from SinglyLinkedList import *
class Solution:
      def removeDuplicates(self,root:Node)->None:
        if not root: return  
        
        prev:Node=None 
        current=root
        next:Node=None 
        
        hash_map={}
        while current:
                next=current.next 
                if current.val not in hash_map:
                    hash_map[current.val]=1 
                    prev=current 
                    current=next 
                else:
                    while next and next.val in hash_map:
                          next=next.next 
                    
                    prev.next=next
                    prev=current 
                    current=next 

class TestApp:  
      def testing_case_two(self):
          node=SinglyLinkedList()
          node.insertAtTail(2)
          node.insertAtTail(3)
          node.insertAtTail(2)
          node.insertAtTail(3)
          node.insertAtTail(2)
          node.insertAtTail(1)
          Solution().removeDuplicates(node.head)
          assert node.convertToList()==[2,3,1]
      def testing_case_three(self):
          node=SinglyLinkedList()
          node.insertAtTail(1)
          node.insertAtTail(2)
          node.insertAtTail(3)
          Solution().removeDuplicates(node.head)
          assert node.convertToList()==[1,2,3]
                    