class Monotonic:
    #descending order array check
    def monotoneDecreasing(array):
        for i in range(len(array)-1):
            if not array[i]>array[i+1]:
                return False
        return True
    #increaing array (ascending order array check)  
    def monotoneIncreasing(array):
        for i in range(len(array)-1):
            if not array[i]<array[i+1]:
                return False
        return True
array=[1,0,-1,-4,-5]
status1=Monotonic.monotoneDecreasing(array)
status2=Monotonic.monotoneIncreasing(array)
if status1 or status2:
    print("Monotonic")
else:
    print("Not a Monotonic")