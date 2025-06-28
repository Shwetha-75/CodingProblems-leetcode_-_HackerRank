def binarySearch(array,left,right,target):
    mid=(left+right)//2
    while left<=right:
        if array[mid]==target:
            return mid
        elif target>array[mid]: return binarySearch(array,mid+1,right,target)
        else: return binarySearch(array,left,mid-1,target)
    return -1


array=[1,2,3,4,5,6]
left=0
right=len(array)-1
target=2
print(binarySearch(array,left,right,target))