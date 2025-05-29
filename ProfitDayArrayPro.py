list1=[7,6,5,4,3,2,1]

profit=0
for i in range(1,len(list1)):
    if list1[i]>list1[i-1]:
        profit+=(list1[i]-list1[i-1])
    
print(profit)
        
    