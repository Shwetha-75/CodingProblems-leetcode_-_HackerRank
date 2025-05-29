def findPairs(array,l,r,n):
    count=0
    i=0
    j=n-1
    while i<=n-1:
        j=i+1
        while j<=n-1:
            print(i,j)
            if array[i]+array[j]>=l and array[i]+array[j]<=r:
                    temp=array[i]^array[j]
                    if temp%2!=0:
                       print(array[i],array[j])
                       count+=1
            j+=1
        i+=1
            
    print("Count: ",count)
findPairs([1,2,3,4],2,10,4)