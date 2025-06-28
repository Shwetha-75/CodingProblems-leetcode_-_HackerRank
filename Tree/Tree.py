class Node:
        def __init__(self,val:int=0):
            self.val=val 
            self.child=[] 
        
class Tree:
        def __init__(self):
            self.root=None 
        def find(self,parent_value):
            temp:Node=self.root 
            queue=[temp]
            while queue:
                  item=queue.pop()
                  if item.val==parent_value: return item 
                  if item.child:
                     queue+=item.child 
            return None 
        def insert(self,parent_value,value):
            node=Node(value)
            if not self.root:
               self.root=node 
               return 
            parent_node=self.find(parent_value)
            if not parent_node:
               return "parent does not exists!!"
            parent_node.child.append(node)
            return 
        def traversal(self):
            temp=self.root 
            queue=[temp]
            while queue:
                  item=queue.pop(0)
                  print(item.val,end=" ")
                  if item.child:
                     queue+=item.child
            print()
        def remove(self,value:int):
            if not self.root:
               return -1 
            if self.root.val == value and not self.root.child:
                self.root=None 
                return value
            if self.root.val == value:
               new_parent:Node=self.root.child.pop(0)
               self.root.val=new_parent.val 
               self.root.child+=new_parent.child
               return value 
            queue=[self.root.child]
            while queue:
                    temp_queue:list[Node]=queue.pop(0)
                    index=0
                    
                    while index < len(temp_queue):
                            
                            if temp_queue[index].val==value:
                                if not temp_queue[index].child:
                                    temp_queue.pop(index)
                                    return value 
                                new_parent=temp_queue[index].child.pop(0)
                                temp_queue[index].val=new_parent.val
                                temp_queue[index].child+=new_parent.child
                                return value 
                            if temp_queue[index].child:
                                queue+=[temp_queue[index].child] 
                                
                            index+=1
                   
            return -1 
        

tree=Tree()
tree.insert(None,1)
tree.insert(1,2)
tree.insert(1,3)
tree.insert(1,4)
tree.insert(2,5)
tree.insert(2,6)
tree.insert(3,7)
tree.insert(4,8)
tree.insert(4,9)
tree.traversal()
tree.remove(4)
tree.traversal()