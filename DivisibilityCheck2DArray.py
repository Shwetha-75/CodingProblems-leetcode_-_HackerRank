def check(array):
    #For array=[1,2,3]
    #num=[[1],[2],[3]]
    num=[[i] for i in array]
    num.sort()#sort the num
   
    for i in range(1,len(array)):
        #when i=1, j=0
        for j in range(i):
            # i=1, j=0 -->array[1]%array[0]-->2%1==0,len(num[i])-->1<len(num[j])+1-->1+1--->1<2
            #           True : nums[1]=nums[j]+[array[i]]=[1]+[2]-->[1,2]
            #i=2, j=0 -->array[2]%array[0]-->3%1==0,len(num[i])-->1<len(num[j])+1-->1+1--->1<2
            #           True : nums[2]=nums[j]+[array[i]]=[1]+[3]-->[1,3]
            #     j=1--->array[2]%array[1]-->3%2!=0,len(num[i])-->1<len(num[j])+1-->1+1--->1<2
            #           False : 
            #nums=[[1],[1,2],[1,3]]
            if array[i]%array[j]==0 and len(num[i])<len(num[j])+1:
                num[i]=num[j]+[array[i]]
                print(num)
                
    print(num)
    return max(num, key=len)

array=[1,2,3]
print(check(array))