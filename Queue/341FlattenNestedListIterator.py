'''
341. Flatten Nested List Iterator
Solved
Medium
Topics
premium lock icon
Companies
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.

 

Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
 

Constraints:

1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-106, 106].
'''

from NestedInteger import NestedInteger
class NestedIterator:
    def __init__(self, nestedList):
        self.array:list[NestedInteger]=[]
        def helper(data:list[NestedInteger]):
            for i in range(len(data)):
                if data[i].isInteger():
                    self.array.append(data[i].getInteger())
                else:
                    helper(data[i].getList())
            return 
        helper(nestedList)
        print(self.array)
        self.size=len(self.array)
        self.index=-1
    def next(self) -> int:
        
        print(self.index,end=' ')
        return self.array[self.index]
        
    
    def hasNext(self) -> bool:
        print("At Has next: ",self.index)
        print(self.index-1<self.size)
        self.index+=1
        
        return self.index<self.size

nestedList=[
    NestedInteger(None,[NestedInteger(1),NestedInteger(1)]),
    NestedInteger(2),
    NestedInteger(None,[NestedInteger(1),NestedInteger(1)]),
    ]
# print(nestedList)
list=NestedIterator(nestedList)

while list.hasNext():
    print(list.next())



