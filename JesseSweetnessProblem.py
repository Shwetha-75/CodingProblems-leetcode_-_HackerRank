def calculate(nums,k):
    def sweet(nums,k):
        num1=nums.pop(0)
        num2=nums.pop(1)
        nums.append(num1+num2*2)
        print(nums)
       
   
    for i in nums:
        nums.sort()
        print(nums)
        if  i<k:
            sweet(nums,k) 
    return nums
nums=[1,2,3,9,10,12]

k=7
print(calculate(nums,k))