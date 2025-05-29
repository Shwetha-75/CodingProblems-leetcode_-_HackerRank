def subSetArrayCreation(array):
    result=[[]]
    for i in range(len(array)):
        subset=[array[i]]
        result.append(subset[::])
        for j in range(i+1,len(array)):
            subset.append(array[j])
            result.append(subset[::])
            subset.pop()
    return result
array=[1,2,3]
print(subSetArrayCreation(array))
            