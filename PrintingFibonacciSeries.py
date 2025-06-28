def fibonacci(n):
    if n==0: return 0
    if n==1: return 1
    prev=0
    current=1
    count=1
    print('0 1',end=" ")
    while count<n: #O(n)
        next=prev+current
        prev=current
        current=next
        print(next,end=" ")
        count+=1
        
fibonacci(5)