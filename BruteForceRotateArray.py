#Brute Force Approach to rotate the array
class RotateArray:
    def rotatingArary(array,k):
        #sub array of size k and the subarray will of last k elements
        auxArray=array[len(array)-k:len(array):]
        print(auxArray)
        #shiftingb the array elements towards right by k steps
        for i in reversed(range(len(array)-k)):
            array[i+k]=array[i]
        #updating the array elements by auxArray within the same positions
        for i in range(k):
            array[i]=auxArray[i] 
         
        return array
print(RotateArray.rotatingArary([1,2,3,4,5,6,7,8,9,10],0))
