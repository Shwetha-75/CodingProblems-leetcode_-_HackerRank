def sequence(nums):
    count=1
    sum=0
    for i in range(1,nums+1):
        temp=1
        for j in range(1,i+1):
          
           temp*=count
           
           count+=1
           
        sum+=temp
    return sum%(pow(10,9)+7)
print(sequence(7))