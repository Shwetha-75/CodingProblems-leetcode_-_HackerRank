array=[0,0,-1,0,-2,-3,9,-10,11]

def swap(array,i,j):
    array[i],array[j]=array[j],array[i]
def partition(array,start=0,end=len(array)-1):
    middle=(start+end)//2
    
    #1 2 3 4 5   5 6 1 2 4
    swap(array,start,middle)
        
    pivot=array[start]
    i=start+1
    j=end
    
    while i<=j:#stopping condition
    #in the case of array elements are already sorted
    #3 2 1 4 5   1 6 5 2 4 ---> 1 4 5 2 6  --> 1 4 5 2 6   -->  1 4 2 5 6
    #              |     | -->  swaped             | |-->swap       | |      
    #              i     j stopped                 i j              j i
    #pivot=3     pivot=1   
        
        
        while i<=len(array)-1 and array[i]<=pivot: #because the left side of pivot should always have lesser than pivot
           
            i+=1
        
        while j>=0 and array[j]>pivot:#becu=ause the right side of pivot should always greater than pivot
             j-=1
        
        if i<j:#if i and j as stopped at particular instance we can swap
            swap(array,i,j)
    swap(array,start,j)
    return j#   3 2 1 4 5           1 4 2 5 6
            #   1 2 3 4 5           2 4 1 5 6
            #  
def quickSort(array,start=0,end=len(array)-1):
    while start<end:
        #then function returns the index where we have to divide subarray
        pivotIndex=partition(array,start,end)
        #we have to consider the lower subarray to make it O(nlogn) time complexity
        if pivotIndex-start<end-pivotIndex:
            quickSort(array,start,pivotIndex-1)
            #after the recursion we have change the start to hold the next subarray
            #to perform quicksort on that
            start=pivotIndex+1
        else:
            quickSort(array,pivotIndex+1,end)
            end=pivotIndex-1
        
quickSort(array)
print(array)