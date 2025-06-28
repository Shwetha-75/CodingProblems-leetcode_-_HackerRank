class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def checkTreeMirror(root1,root2):
    if root1==None and root2==None: return True
    if root1==None or root2==None or root1.val!=root2.val : 
        return False
   
    return checkTreeMirror(root1.left,root2.left) and checkTreeMirror(root1.right,root2.right)
def main():
    root1=Node(1)
    root1.left=Node(1)
    root1.right=Node(2)
    root1.left.left=Node(3)
    root1.left.right=Node(1)
    root1.right.left=Node(6)
    root1.right.right=Node(4)
    root2=Node(1)
    root2.left=Node(1)
    root2.left.left=Node(3)
    root2.left.right=Node(1)
    root2.right=Node(2)
    root2.right.left=Node(6)
    root2.right.right=Node(4)
    print(checkTreeMirror(root1,root2))
main()
    