class Solution:
    # instance variables storing the elements on to the stack
    def __init__(self):
        self.inStack=[]   # pushing all the elements on to the stack
        self.outStack=[]  # popping out the all the elements from the stack
        # push operation
    def push(self,value):
        self.inStack.append(value)
        # pop opertion removing the element from the stack at 0th indexed
    def pop(self):
        temp=self.inStack.pop(0)
        # appending it to the outstack 
        self.outStack.append(temp)
        return temp 
    # getting the 0th indexed element
    def peek(self):
        return self.inStack[0]
    # checking for the stack is empty or not
    def empty(self):
        return len(self.inStack)==0
def main():
    solution=Solution()
    solution.push(10)
    solution.push(20)
    solution.push(30)
    solution.push(40)
    solution.push(50)
    solution.push(60)
    print(solution.inStack)
    print(solution.pop())
    print(solution.inStack)
    print(solution.outStack)
    print(solution.peek())
    print(solution.empty())
    solution.pop()
    solution.pop()
    solution.pop()
    solution.pop()
    solution.pop()
    print(solution.empty())
    print(solution.inStack)
    print(solution.outStack)
    
main()
    