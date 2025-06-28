import sys
class Node:
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None
        
def preOrder(root,list1):
    if root==None: return
    list1.append(root.val)
    preOrder(root.left,list1)
    preOrder(root.right,list1)
    
    
def main():
    root=Node(4)
    root.left=Node(2)
    root.right=Node(6)
    root.left.left=Node(1)
    root.left.right=Node(3)
    list1=[]
    preOrder(root,list1)
    print(list1)
    n=len(list1)
    minElm=sys.maxsize
    for i in range(n):
        for j in range(i+1,n):
            minElm=min(minElm,abs(list1[i]-list1[j]))
    print(minElm)
    
main()