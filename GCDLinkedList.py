'''
Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 

Example 1:


Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
There are no more adjacent nodes, so we return the linked list.
Example 2:


Input: head = [7]
Output: [7]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.
 

Constraints:

The number of nodes in the list is in the range [1, 5000].
1 <= Node.val <= 1000.
'''
from SinglyLinkedList import Node,LinkedList
class Solution:
    def gcdLinkedLisat(self,head:Node):
        def helper(num1,num2):
            result=min(num1,num2)
            while result:
                if num1%result==0 and num2%result==0:
                    break
                result-=1
            # print(result)
            return result
        if head.next:
            current=head
            nxt=current.next 
            while nxt:
                  num1=current.value
                  num2=nxt.value
                #   print(num1,num2)
                  node=Node(helper(num1,num2))
                  print(node.value)
                  temp=nxt
                  current.next=node
                  node.next=temp 
                  current=nxt 
                  nxt=nxt.next 
        return head 
def main():
    sol=Solution()
    node=LinkedList()
    node.addAtTail(18)
    node.addAtTail(6)
    node.addAtTail(10)
    node.addAtTail(3)
    res=sol.gcdLinkedLisat(node.head)
    node.printing(res)
main()