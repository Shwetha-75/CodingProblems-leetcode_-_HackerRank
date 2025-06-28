def groupAnagrmas(string):
    list1=[]
    for i in string:
        list1.append(''.join(sorted(i)))
    dict1={}
    for i,e in enumerate(list1):
        if e not in dict1:
            dict1[e]=[string[i]]
        else:
            dict1[e].append(string[i])
    li=[]
    for i,el in enumerate(dict1):
        li.append(dict1[el])
    print(li)
        
string=["abc","atc","peacock","tca","stf","listen","silent"]
groupAnagrmas(string)

