def sumElements(array,power=1):
    #store the sum of array elements
    sum=0# O(1)   0()-->average omg()-->best
    for i in array:#                                 time complexity-->  O(n)-->
        if type(i)==list:#
            sum+=sumElements(i,power+1)#        space complexity --> depth of the array--> calls the function--> call stacks will be created 
        else:#                                            O(d)-->max depth
            sum+=i
    return pow(sum,power)
array=[1,2,[2,3],[[2]]]   #(1+2+(2+3)^2+((2)^3)^2)-->(1+2+25+(8)^2)--> (28+64)-->92
print(sumElements(array))