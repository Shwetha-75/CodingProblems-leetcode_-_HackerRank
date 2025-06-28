class Node:
      def __init__(self,val:int=0):
          self.val=val 
          self.left=None 
          self.right=None 

class BinaryTree:
        def __init__(self):
            self.root=None 
            self.head=None
        def insert(self,val:int=0):
            node=Node(val)
            if not self.root:
               self.head=node
               self.root=node 
               return 
            queue=[self.root]
            while queue:
                  top=queue.pop(0)
                  if not top.left:
                      top.left=node 
                      return 
                  if not top.right:
                      top.right=node 
                      return 
                  queue.append(top.left)
                  queue.append(top.right)
            return 
        def remove(self,root:Node,value:int=0,parentNode:Node=None):
            if not root:
               return
            if root.val==value and not parentNode and root.left and root.right:
            #  recursively call the function to remove the node 
            # find out the left descent value  
                 value=self.leftDescendent(root)
                 root.val=value 
                 self.remove(root.left,value,root)
                 return
            if root.val==value and not parentNode and (not root.left or not root.right):
                if root.left:
                   temp=root.left 
                   root.left=None 
                   root=temp 
                if root.right:
                    temp=root.right 
                    root.right=None 
                    root=temp 
                return 
            if parentNode:
                
                if parentNode.left and parentNode.left.val==value:
                    if parentNode.left.left and parentNode.left.right:
                       #find the left descendent
                       result=self.leftDescendent(parentNode.left)
                       print("Printing the result : ",result)
                       parentNode.left.val=result
                       self.remove(parentNode.left,result,parentNode)
                       return
                    elif parentNode.left.left and not parentNode.left.right:
                         temp=parentNode.left.left 
                         parentNode.left.left=None 
                         parentNode.left=temp 
                        
                    elif parentNode.left.right and parentNode.left.left:
                         temp=parentNode.left.right 
                         parentNode.left.right=None 
                         parentNode.left.right=temp 
                         
                    else:parentNode.left=None
                     
                    return 
                if parentNode.right and parentNode.right.val==value:
                    if parentNode.right.left and parentNode.right.right:
                        value=self.leftDescendent(parentNode.right)
                        parentNode.right.val=value 
                        self.remove(parentNode.right,value,parentNode)
                        return
                    elif parentNode.right.left and not parentNode.right.right:
                         temp=parentNode.right.left 
                         parentNode.right.left=None 
                         parentNode.right=temp 
                    elif parentNode.right.right and not parentNode.right.left:
                         temp=parentNode.right.right 
                         parentNode.right.right=None 
                         parentNode.right=temp 
                    else:
                        parentNode.right=None 
                        
                    return 
            self.remove(root.left,value,root)
            return       
                    
            # find the left descendent leaf node  
        def leftDescendent(self,root:Node)->int:
            if not root.left and not root.right:
               print(root.val)
               return root.val
            self.leftDescendent(root.left)
            self.leftDescendent(root.right)
        
        
        def inOrder(self,root:Node):
            if not root:
               return 
            print(root.val,end=" ")
            self.inOrder(root.left)
            self.inOrder(root.right)

node=BinaryTree()
node.insert(1)
node.insert(2)
node.insert(3)
node.insert(4)
node.insert(5)
node.insert(6)
node.insert(7)
node.insert(8)
node.insert(9)
node.inOrder(node.head)
node.remove(node.head,2)
print("")
node.inOrder(node.head)


            