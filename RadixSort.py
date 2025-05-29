
import math
def radixSort(array):
    maxNumber=max(array)
    #finding the max number of digits to perform counting sort at each digit places
    maxDigit=math.floor(math.log10(maxNumber))+1
    #calling counting sort-->upto maxDigit
    for i in range(maxDigit):
        countingSort(array,i)
    return array
def countingSort(array,digitPlace):
    result=[0]*len(array)
    temp=[0]*10 #frequncy of each digit and as well as taking cummulative sum
    #taking single digit from array elements at each digitplace
    divideNumber=math.pow(10,digitPlace)
    
    #traversing through the array elements
    for i in array:
        #finding the single digit at digiplace(unit,tens,hundreds)
        single=math.floor(i/divideNumber)%10
        #counting the frequencies
        #[284,31,7,45,8,90]
        #[4,1,7,5,8,0]-->single digit at unit place
        #
        #
        #
        #
        #
        temp[single]+=1
    #cummulative sum
    for i in range(1,10):
        temp[i]=temp[i-1]+temp[i]
    #at the resultant array we are going to insert each elements
    
    #traverse the array elements in reverse direction
    for i in reversed(array):
        #to find the index at temp array
        cur=math.floor(i/divideNumber)%10
        #to drcrement value at cur index
        temp[cur]-=1
        #the value would be index positon to insert at result array
        result[temp[cur]]=i
    #should copy to array
    for i in range(len(result)):
        array[i]=result[i]
array=[284,31,7,45,8,90]
print(radixSort(array))
    