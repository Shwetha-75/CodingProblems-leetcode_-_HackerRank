string='ABCDCDC'
subString='CDC'
count=0
for i in range(len(string)-(len(subString)-1)):
    var=''
    for j in range(len(subString)):
        var+=string[i+j]
        print(var)
    if var==subString:
        count+=1
print(count)