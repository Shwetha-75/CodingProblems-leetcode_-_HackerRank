import sys
def subArray(array,target):
    min1=sys.maxsize
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i:j+1:])
            if target==sum(array[i:j+1:]):
                  print("target",array[i:j+1:])
                  min1=min(min1,len(array[i:j+1:]))
              
    print(min1)
target=11       
subArray([1,1,1,1,1,1,1,1],target)