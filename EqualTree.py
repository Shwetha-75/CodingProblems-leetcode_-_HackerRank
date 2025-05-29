class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val 
        self.left=left
        self.right=right
def isSame(pTree,qTree):
    if pTree==None and qTree==None:
        return True
    if pTree==None or qTree==None or pTree.val!=qTree.val:
        return False
    return isSame(pTree.left,qTree.left) and isSame(pTree.right,qTree.right)
def main():
    rootp=TreeNode(10)
    rootp.left=TreeNode(20)
    rootp.left.left=TreeNode(-30)
    rootp.left.right=TreeNode(40)
    rootp.right=TreeNode(50)
    rootp.right.left=TreeNode(60)
    rootp.right.right=TreeNode(70)
    rootq=TreeNode(-10)
    rootq.left=TreeNode(20)
    rootq.left.left=TreeNode(30)
    rootq.left.right=TreeNode(40)
    rootq.right=TreeNode(50)
    rootq.right.left=TreeNode(60)
    rootq.right.right=TreeNode(70)
    print(isSame(rootp,rootq))
main()
    