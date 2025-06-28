class Node:
    def __init__(self,val):
        self.val=val 
        self.left=None 
        self.right=None 

class Solution:
    def zigzagLevelOrder(self, root:Node):
        queue=[(root,0)]
        result:list[list[int]]=[]
        while queue:
              node:Node=queue.pop(-1)
              if len(result)>node[1]:
                  result[-1].append(node.val)
              else:
                  result.append([node.val])
              if node.left:
                  queue.append((node.left,node[1]+1))
              if node.right:
                  queue.append((node.right,node[1]+1))
        for i in range(len(result)):
            if i%2:
               result[i]=result[i][::-1]
        return result 