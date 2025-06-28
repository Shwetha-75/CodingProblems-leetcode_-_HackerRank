class TreeNode:
    def __init__(self,val):
        self.val=val#             <--[left,val,right]-->root node
        self.left=None#              /               \
        self.right=None# <--[left,val,right]      <--[left,val,right]
#                            /          \               /          \
#              [left,val,right]  [left,val,right] [left,val,right] [left,val,right]


#traversal
#InorderTraversal
def printInorderTraversal(root):
    if root:
        printInorderTraversal(root.left)
        print(root.val,end=' ')
        printInorderTraversal(root.right)

#PreOrderTraversal
def printPreorderTraversal(root):
    if root:
        print(root.val,end=' ')
        printPreorderTraversal(root.left)
        printPreorderTraversal(root.right)

#PostOrderTraversal

def printPostorderTraversal(root):
    if root:
        printPostorderTraversal(root.left)
        printPostorderTraversal(root.right)
        print(root.val,end=' ')

def main():
    root=TreeNode(0)                              #    0-->root node
    root.left=TreeNode(-3)                        #   / \
    root.right=TreeNode(5) #  left sub tree <--    -3     5-->right sub tree
    root.left.left=TreeNode(-10)#                  /       \
    root.right.right=TreeNode(9)#                -10        9--> right leaf node
    print()#                                      |
    print("Inorder Traversal",end=' ')#       left leaf node           
    printInorderTraversal(root)#         
    print("Preorder Traversal",end=' ')#
    printPreorderTraversal(root)
    print()
    print("Post Traversal",end=' ')
    printPostorderTraversal(root)
main()
   
    
    