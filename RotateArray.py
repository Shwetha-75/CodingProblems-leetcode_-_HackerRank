array=[1,2,3,4,5,6,7]
k=3
#complexity is worse O(n^2)
for i in range(k):
    temp=array[len(array)-1]
    for j in reversed(range(len(array))):
        if j==0:
            break
        else:
            array[j]=array[j-1]
    array[0]=temp
    print(array)
