from Tree import Tree 

class Solution:
      def __init__(self):
          self.arr=[]
      def inOrder(self,root:Tree):
          if not root:
            return 
          self.arr.append(root.val)
          self.inOrder(root.left)
          self.inOrder(root.right) 
      def findTarget(self,root:Tree,target:int):
          self.inOrder(root)
          hash_map={}
          for num in self.arr:
              if target-num in hash_map:
                  return True 
              if num in hash_map:
                  hash_map[num]+=1 
              else:
                  hash_map[num]=1
          return False 
          