array=[]
target=1
for i in range(len(array)):
    temp=array[:i+3]
    if len(temp)==3:
        sumArray=sum(temp)
        if sumArray==target-1 or sumArray==target+1:
             print(sumArray)
    else:
        break
        