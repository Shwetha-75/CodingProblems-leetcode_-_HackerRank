def maxJump(array,n):
    maxJump=0
    for i in range(n):
        if i>maxJump:
            return 0
        if array[i]+i>maxJump:
            maxJump=array[i]+i 
    return 1
array=[3,1,2,1,7]
print(maxJump(array,5))
            