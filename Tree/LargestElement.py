from BinaryTree import Node
class Solution:
        def largestValues(self, root:Node):
            result=[]
            queue=[root]
            while queue:
                  length=len(queue)
                  max_element=float('-inf')
                  for _ in range(length):
                      element:Node=queue.pop(0)
                      if max_element<element.val:
                         max_element=element.val
                      if element.left:
                          queue.append(element.left)
                      if element.right:
                          queue.append(element.right)
                  result.append(max_element)
            return result
      