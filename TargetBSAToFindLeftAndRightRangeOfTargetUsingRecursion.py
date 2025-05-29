array=[9,9,9,9,9,9,9,9,9,9,9]
target=0
range=[-1,-1]
#funtion to find the left extreme end
def findLeftExtreme(array,target,range,left=0,right=len(array)-1):
    #find mid value
    mid=(left+right)//2
    #stopping condition
    if left>right: return
    #if target found
    if array[mid]==target:
            #case 1: if we have reached left extreme of the array object
            if mid==0: 
                #then 0 id the left extreme end
                range[0]=mid
                return 
            #case 2: recursively calling the function 
            #by changing the right pointer to have mid-1
            #performing BSA again
            elif array[mid-1]==target: findLeftExtreme(array,target,range,left,mid-1)
            else: 
                #found left range
                range[0]=mid
                return 
    #BSA condition to change left or right pointers 
    #call function recursively
    elif target>array[mid]:
           findLeftExtreme(array,target,range,mid+1,right)
    else:
           findLeftExtreme(array,target,range,left,mid-1)
#funtion to find the right extreme end
def findrightExtreme(array,target,range,left=0,right=len(array)-1):
     #find mid value
    mid=(left+right)//2
    #stopping condition
    if left>right: return
    #if target found
    if array[mid]==target:
        #case 1: if we have reached right extreme of the array object
        if mid==len(array)-1:
            #then len(array)-1 is the right extreme end
            range[1]=mid
            return
         #case 2: recursively calling the function 
            #by changing the left pointer to have mid+1
            #performing BSA again
        elif array[mid+1]==target: findrightExtreme(array,target,range,mid+1,right)
        else:#found range (right)
            range[1]=mid
            return
     #BSA condition to change left or right pointers 
    #call function recursively
    elif target>array[mid]:
        findrightExtreme(array,target,range,mid+1,right)
    else:
        findrightExtreme(array,target,range,left,mid-1) 
    

findLeftExtreme(array,target,range)
findrightExtreme(array,target,range)
print(range)

   