class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def printPreOrderTree(root):
        if root==None: return 
        print(root.val,end=" ")
        printPreOrderTree(root.left)
        printPreOrderTree(root.right)
            
def printInOrderTree(root):
        if root==None: return
        printInOrderTree(root.left)
        print(root.val,end=" ")
        printInOrderTree(root.right)
def printPostOrderTree(root):
        if root==None: return
        printPostOrderTree(root.left)
        printPostOrderTree(root.right)
        print(root.val,end=" ")
class Solution:
    def sortToBST(self,array):
        if len(array)==0:#Observation
            return None#
        mid=len(array)//2# 5//2-->2
        root=TreeNode(array[mid])
        root.left=(self.sortToBST(array[:mid]))
        root.right=(self.sortToBST(array[mid+1:]))
        return root
def main():
    array=[-10,-3,0,5,9]#
    s=Solution()#
    root=s.sortToBST(array)
    printPreOrderTree(root)
    print()
    printInOrderTree(root)
    print()
    printPostOrderTree(root)
main()
    
    
           