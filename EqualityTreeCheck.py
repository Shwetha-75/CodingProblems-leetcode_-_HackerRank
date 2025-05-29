class Node():
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None
#method that checks whether both tree are equal or not
def checkEquality(root1,root2):
    if root1==None and root2==None:
        return True
    if root1.val!=root2.val:
        return False
    #calling the function recursively
    return checkEquality(root1.left,root2.left) and checkEquality(root1.right,root2.right)
    
def main():
    root1=Node(1)
    root1.left=Node(2)
    root1.left.left=Node(3)
    root1.left.right=Node(3)
    root1.right=Node(4)
    root1.right.left=Node(5)
    root1.right.right=Node(6)
    
    root2=Node(1)
    root2.left=Node(2)
    root2.left.left=Node(3)
    root2.left.right=Node(3)
    root2.right=Node(4)
    root2.right.left=Node(5)
    root2.right.right=Node(6)
    print(checkEquality(root1,root2))
main()
    
    
    