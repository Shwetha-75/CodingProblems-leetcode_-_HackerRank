list1=[1,2]
list2=[1,2,3,4,5]
dict1={}
for i in list2:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1
result=[]
for i in list1:
    if i not in dict1:
       