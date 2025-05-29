def superFunction(num):
    sum=0
    while num!=0:
        rev=num%10
        sum+=rev
        num//=10
    if sum<=9: return sum
    else:
        return superFunction(sum)
num='123'
k=3
str1=num.ljust(len(num)*k,num)
str2=""

print(str1)
print(superFunction(148148148))