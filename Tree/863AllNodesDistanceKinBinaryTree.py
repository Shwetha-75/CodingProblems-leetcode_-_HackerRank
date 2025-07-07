'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000

'''

from BinaryTree import Node as TreeNode
class Solution:
     def __init__(self):
         self.array:list[TreeNode]=[]
     def preOrder(self,root:TreeNode):
         if not root:
             return 
         self.array.append(root)
         self.preOrder(root.left)
         self.preOrder(root.right)
         
     def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
         self.preOrder(root)
         result=[]
         for node in self.array:
             if node==target:
                 continue 
             lca=self.lca(root,target,node)
             d1=self.findLength(lca,target,0)
             d2=self.findLength(lca,node,0)
             if d1+d2==k:
                 
                 result.append(node.val)
         return result

     def findLength(self,root:TreeNode,node:TreeNode,level:int):
         if not root:
             return -1 
         if root.val==node.val:
            return level 
         left=self.findLength(root.left,node,level+1)
         if left==-1:
             return self.findLength(root.right,node,level+1)
         return left 
     def lca(self,root:TreeNode,node1:TreeNode,node2:TreeNode):
         if not root: 
             return None
         if root.val==node1.val or root.val==node2.val:
             return root 
         left=self.lca(root.left,node1,node2)
         right=self.lca(root.right,node1,node2)
         if not left and not right:
             return None 
         if left and right: 
             return root 
         return left if left else right 


#                     3        target=5, k=2
#                  /     \ 
#                 5       1
#                  \     /  \
#                   2   0    8            
#                 /   \
#                7     4

#  Approach :
#  
#  Step 1: lca=Find the Lowest Common Ancestor between both the nodes 
#  Step 2: find the distance1 and distance2 
#           add the distance1+distance2 and check if its equal to k then  
#                add the current node val to the result array6
        
