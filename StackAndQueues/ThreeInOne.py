class Stack:
        def __init__(self):
            self.stack:list[list[int]]=[[],[],[]]
        def pushStack1(self,val):
            self.stack[0].append(val)
        def pushStack2(self,val):
            self.stack[1].append(val)
        def pushStack3(self,val):
            self.stack[2].append(val)
        def popStack1(self):
            if not self.stack[0]:
                return None 
            return self.stack[0].pop(-1)
        def popStack2(self):
            if not self.stack[1]:
                return None 
            return self.stack[1].pop(-1)
        def popStack3(self):
            if not self.stack[2]:
                return None 
            return self.stack[2].pop(-1)
        def peekStack1(self):
            if not self.stack[0]:
                return None 
            return self.stack[0][-1]
        def peekStack2(self):
            if not self.stack[1]:
                return None 
            return self.stack[1][-1]
        def peekStack3(self):
            if not self.stack[2]:
                return None 
            return self.stack[2][-1]
        def displayStack1(self):
            for ele in self.stack[0]:
                print(ele,end=" ")
            print()
        def displayStack2(self):
            for ele in self.stack[1]:
                print(ele,end=" ")
            print()
        def displayStack3(self):
            for ele in self.stack[2]:
                print(ele,end=" ")
            print()


stack=Stack()
stack.pushStack1(10)        
stack.pushStack1(20)
stack.pushStack1(30)
stack.pushStack1(40)
stack.pushStack1(50)
stack.displayStack1()
print(stack.peekStack1())
stack.popStack1()
stack.popStack1()
stack.popStack1()
stack.popStack1()
stack.popStack1()
stack.displayStack1()