n=5
dict1=[0,1]
for i in range(2,n):
  
    dict1.append(dict1[i-2]+dict1[i-1])
print(dict1)
    