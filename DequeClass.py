'''
A deque is a double-ended queue. It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same  performance in either direction.

Click on the link to learn more about deque() methods.
Click on the link to learn more about various approaches to working with deques: Deque Recipes.

Example

Code

>>> from collections import deque
>>> d = deque()
>>> d.append(1)
>>> print d
deque([1])
>>> d.appendleft(2)
>>> print d
deque([2, 1])
>>> d.clear()
>>> print d
deque([])
>>> d.extend('1')
>>> print d
deque(['1'])
>>> d.extendleft('234')
>>> print d
deque(['4', '3', '2', '1'])
>>> d.count('1')
1
>>> d.pop()
'1'
>>> print d
deque(['4', '3', '2'])
>>> d.popleft()
'4'
>>> print d
deque(['3', '2'])
>>> d.extend('7896')
>>> print d
deque(['3', '2', '7', '8', '9', '6'])
>>> d.remove('2')
>>> print d
deque(['3', '7', '8', '9', '6'])
>>> d.reverse()
>>> print d
deque(['6', '9', '8', '7', '3'])
>>> d.rotate(3)
>>> print d
deque(['8', '7', '3', '6', '9'])
Task

Perform append, pop, popleft and appendleft methods on an empty deque .

Input Format

The first line contains an integer , the number of operations.
The next  lines contains the space separated names of methods and their values.

Constraints


Output Format

Print the space separated elements of deque .

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft

Sample Output

1 2

'''

from collections import deque

test=int(input())

queue=deque()

for i in range(test):
    string=input()
    if string[0]=='append':
        queue.append(int(string[1]))
    if string[0]=='appendleft':
        queue.appendleft(int(string[1]))
    if string[0]=='pop':
        queue.pop()
    if string[0]=='popleft':
        queue.popleft()
for i in queue:
    print(i,end=' ')