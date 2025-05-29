list1=[0,0,1,1,1,1,2,3,3]
#here we have to remove the element which as occured more than twice
#  we  since we can only unquie twice or once
dict1={}
#traversing through list elements
for i in list1:
    #storing the elements in dict as key number of occurrence as value
    if i in dict1:
        #the value should be less than two 
        if dict1[i]<2:
            dict1[i]+=1
    else:#first occurrence
        dict1[i]=1
print(dict1)
#removing all the list elements
list1.clear()
print(list1)
#traversing through dict1
for i in dict1:
    #if the value as occurred twice the appending two times
        if dict1[i]==2:
            list1.append(i)
            list1.append(i)
    # or else once
        else:
            list1.append(i)
print(list1)

