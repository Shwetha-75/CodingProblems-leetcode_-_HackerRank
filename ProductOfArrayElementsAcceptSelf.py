from functools import *
def product(array):
   dict1={}
   for i in range(len(array)):
       if i==0:
           dict1[i]=array[1::]
       elif i==len(array)-1:
           dict1[i]=array[:len(array)-1:]
       else:
           dict1[i]=array[:i:]+array[i+1::]
   for i in range(len(array)):
       array[i]=reduce(lambda i,j:i*j,dict1[i])
   return array
print(product([1,2,3,4]))
        
def p(nums):
    temp=1
    nums1=[]
    for i in range(len(nums)):
        pro=temp
        print(pro)
        for j in range(len(nums)):
            if i==j:
                continue
            pro*=nums[j]
            print(pro)
        nums1.append(pro)
        
    print(nums1)
p([1,2,3,4])
    