class RotateArray:
    def rotatingArray(obj,array,k):
       n=len(array)
       k%=n
       def reverse(left,right):
           while left<right:
               array[left],array[right]=array[right],array[left]
               left+=1
               right-=1
               
       reverse(0,n-1)#reversing all array elements
       reverse(0,k-1)#reversing 0, k-1 array elements
       reverse(k,n-1)#reversing k,n-1 array elements
       return array
object=RotateArray()
print(object.rotatingArray([1,2,3,4,5,6,7,8,9,10],5))