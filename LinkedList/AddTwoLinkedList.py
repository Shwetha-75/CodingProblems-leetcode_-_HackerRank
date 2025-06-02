class ListNode:
      def __init__(self,val:int=0):
          self.val=val 
          self.next=None 
        
class Solution:
      def __init__(self):
          self.head=None 
          self.tail=None
      def insert(self,value):
          node=ListNode(value)
          if not self.head:
              self.head=node
              self.tail=node 
              return 
          self.tail.next=node 
          self.tail=node 
              
      def addTwoNumbers(self, l1:ListNode, l2:ListNode):
          carry=0
          l1=self.reverse(l1)
          l2=self.reverse(l2)
          result=None 
          while l1 and l2:
                sum=l1.val+l2.val+carry 
                carry=sum//10
                sum%=10 
                self.insert(sum)
                l1=l1.next 
                l2=l2.next 
          while l1:
                sum=l1.val+carry 
                carry=sum//10 
                sum%=10
                self.insert(sum)
                l1=l1.next 
          while l2:
              sum=l2.val+carry
              carry=sum//10 
              sum%=10
              self.insert(sum)
              l2=l2.next 
          if carry==1:
              self.insert(carry)
          return self.reverse(self.head) 
                
                
      def reverse(self,linkedList:ListNode):
          
          prev=None
          temp=linkedList
          while temp:
                next=temp.next 
                temp.next=prev 
                prev=temp 
                temp=next 
          return prev 
                              
                              
                              
                              
                              