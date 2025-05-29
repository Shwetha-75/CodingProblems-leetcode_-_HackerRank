n=5
for i in range(1,n+1):
    #spaces
    for j in reversed(range(i,n)):
        print(" ",end=' ')
    for k in range(1,2*i):
        if i==1 and j==1:
            print('a',end=" ")
        elif k==1:
            print('/',end=" ")
        elif k==2*i-1:
            print('\\',end=' ')
        else: print(' ',end=' ')
    print()
    