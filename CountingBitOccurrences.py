#convert decimal to binary
list1=[]
def decimal(n):
    if n>=1:
        decimal(n//2)
    list1.append(n%2)
decimal(10)
print(list1.count(1))
