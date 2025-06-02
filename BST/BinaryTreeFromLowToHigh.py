class TreeNode:
      def __init__(self,val:int=0):
          self.val=val
          self.left=None 
          self.right=None 
class Solution:
        def __init__(self):
            self.array=[]
            self.root=None
        def preOrder(self,root:TreeNode):
            if not root:
                return root
            self.array(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)
        def insert(self,value):
            node=TreeNode(value)
            if not self.root:
               self.root=node 
            temp=self.root
            while True:
                  if value<temp.val:
                      if not temp.left:
                         temp.left=node 
                         return 
                      temp=temp.left
                  else:
                      if not temp.right:
                         temp.right=node 
                         return 
                      temp=temp.right     
        def trimBST(self, root:TreeNode, low: int, high: int) ->TreeNode:
            if not root:
                 return root 
            array=[]
            #BFS
            for num in self.array:
                if num>=low and num<=high:
                    array.append(num)
            for num in array:
                self.insert(num)
            return self.root
            
                  