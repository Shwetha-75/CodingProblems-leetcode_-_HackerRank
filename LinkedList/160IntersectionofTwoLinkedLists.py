from SinglyLinkedList import* 

class Solution:
        def getIntersectionNode(self, headA:Node, headB:Node) ->Node:
            hash_map_list1={}
            while headA:
                  hash_map_list1[headA]=1 
                  headA=headA.next
            while headB:
                  if headB in hash_map_list1:
                      return headB 
                  headB=headB.next
            return None 

class TestApp:
      def testing_case_one(self):
          node_1=SinglyLinkedList()
          node_1.insertAtTail(1)
          node_1.insertAtTail(9)
          node_1.insertAtTail(1)
          node_2=SinglyLinkedList()
          node_2.insertAtTail(3)
          node_3=SinglyLinkedList()
          node_3.insertAtTail(2)
          node_3.insertAtTail(4)
          node_1.tail.next=node_3.head 
          node_2.tail.next=node_3.head 
          assert Solution().getIntersectionNode(node_1.head,node_2.head)==node_3.head 
      def testing_case_two(self):
          node_1=SinglyLinkedList()
          node_1.insertAtTail(4)
          node_1.insertAtTail(1)
          node_2=SinglyLinkedList()
          node_2.insertAtTail(5)
          node_2.insertAtTail(6)
          node_2.insertAtTail(1)
          node_3=SinglyLinkedList()
          node_3.insertAtTail(8)
          node_3.insertAtTail(4)
          node_3.insertAtTail(5)
          node_1.tail.next=node_3.head 
          node_2.tail.next=node_3.head 
          assert Solution().getIntersectionNode(node_1.head,node_2.head)==node_3.head
          