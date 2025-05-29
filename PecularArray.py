def sumPower(array,power=1):
    sum=0
    #ierating over array elements
    for i in array:
        #checking whether the ith element is array or integer element
        if type(i)==list:
            #calling the function recursively to sum up the sub array elements
            sum+=sumPower(i,power+1)
        else:
            #if it is element means suming the array elements
            sum+=i
    return sum**power#suppose [[[2]]]--> in this case 2 is present in third call which means
#[[[2]^3]^2]^1-->outer array bounds will have have pow of 1
             #-->inner array bound will have a pow of 2 since it is present in second [[]]
             #inner most will have a pow of 3 since it i present in third [[[]]]
array=[1,2,[2,3],[[2]]]
print(sumPower(array))