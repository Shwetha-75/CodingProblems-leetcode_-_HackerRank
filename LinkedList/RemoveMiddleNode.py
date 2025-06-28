from SinglyLinkedList import * 
class Solution:
      def deleteMiddle(self, head:Node) ->Node:
            length=0 
            temp=head 
            while temp:
                  length+=1 
                  temp=temp.next 
            
            middle=(length//2)+1 
            prev=None 
            curr=head
            length=0
            if head.next==None:
                return None 
            while curr:
                  length+=1 
                  
                  if middle==length:
                     prev.next=curr.next
                     curr.next=None 
                     return head 
                  prev=curr 
                  curr=curr.next 
            return head 

class TestApp:
        def testing_case_one(self):
            node=SinglyLinkedList()
            node.insertAtTail(1)
            node.insertAtTail(2)
            node.insertAtTail(3)
            node.insertAtTail(4)
            node.insertAtTail(5)
            assert node.convertToList(Solution().deleteMiddle(node.head))==[1,2,4,5]
            
        def testing_case_two(self):
            node=SinglyLinkedList()
            node.insertAtTail(1)
            node.insertAtTail(2)
            node.insertAtTail(3)
            node.insertAtTail(4)
            node.insertAtTail(5)
            node.insertAtTail(6)
            assert node.convertToList(Solution().deleteMiddle(node.head))==[1,2,3,5,6]
        def testing_case_(self):
            node=SinglyLinkedList()
            node.insertAtTail(1)
            assert node.convertToList(Solution().deleteMiddle(node.head))==[]
            
        