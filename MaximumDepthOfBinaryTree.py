class Node:
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None
def maxDepth(root):
    if root==None: return 0
    else:
        return max(maxDepth(root.left),maxDepth(root.right))+1
    
def main():
    root=Node(10)
    root.left=Node(20)
    root.right=Node(40)
    root.right.left=Node(-10)
    root.right.left.left=Node(12)
    root.right.left.left.right=Node(13)
    root.right.right=Node(11)
    print(maxDepth(root))
main()