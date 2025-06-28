from SinglyLinkedList import Node as ListNode
class Solution:
      def mergeKLists(self,lists:list[ListNode]):
          if not lists: return None 
          head=lists[0]
          for i in range(1,len(lists)):
              head=self.mergeTwo(head,lists[i])
          return head
      def mergeTwo(self,list1:ListNode,list2:ListNode):
        dummy=tail=ListNode(0)
        while list1 and list2:
              if list1.val<list2.val:
                 tail.next=list1
                 list1=list1.next 
              else:
                tail.next=list2
                list2=list2.next 
              tail=tail.next 
        while list1:
              tail.next=list1
              list1=list1.next
              tail=tail.next 
        while list2:
            tail.next=list2
            list2=list2.next 
            tail=tail.next 
        return dummy.next