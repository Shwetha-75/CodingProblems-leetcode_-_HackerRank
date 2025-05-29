class TargetValue:
    def indicesFind(array,target):
        listIndices=[]
        for i in range(len(array)-1):
            sum=0
            for j in range(i+1,len(array)):
                if array[i]+array[j]==target:
                    listIndices.append(i)
                    listIndices.append(j)
                    return listIndices
        return listIndices
array=[5,4,3,2]
target=7
print(TargetValue.indicesFind(array,target))
            
                
        