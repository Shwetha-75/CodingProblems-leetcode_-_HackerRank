n=5
for i in range(1,n+1):
    for k in reversed(range(n*2-2*i)):
           print('-',end='')
    for j in range(1,2*i):
        if j==1 or j==(2*i-1):
           print(chr(n-1+97),end='-')
        elif j-1>(2*i-1)//2:
            print(chr(n-j+2+97),end='-')
        else:
            print(chr(n-j+97),end='-')
    for k in reversed(range(n*2-2*i)):
           print('-',end='')
    print()
for i in range(2,n+1):
   
    for k in range(2,i*2):
           print('-',end='')
    for j in range((n*2+1)-(2*i)):
        if j==0 or j==(n*2+1)-(2*i)-1:
            print(chr(n-1+65).lower(),end='-')
        else:
            print(chr(n-j-1+65).lower(),end='-')
    for k in range(2,i*2):
           print('-',end='')
    print()
    