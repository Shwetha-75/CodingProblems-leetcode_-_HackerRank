n=5

for i in range(1,n+1):
    count=2
    for j in range(i,n):
        print(" ",end="")
    for k in range(1,2*i):
        if k==1 or k==2*i-1:#Outer boundary 1
            print("1",end="")
        else:
            if k<=(2*i)//2:#inner filling in incremental fasion
                print(count,end="")
                count+=1
            else:
                if k==((2*i)//2)+1: count-=2#inner fiilings in decremental fasion
                print(count,end="")
                count-=1
    print()

for i in range(2,n+1):
    count1=2
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,(n*2+1)-(2*i)+1):
        if k==1 or k==(n*2+1)-(2*i):
            print("1",end="")
        else:
             if k<=((n*2+1)-(2*i)+1)//2:
                 print(count1,end="")
                 count1+=1
             else: 
                 if k==(((n*2+1)-(2*i)+1)//2)+1: count1-=2
                 print(count1,end="")
                 count1-=1
        
    print()