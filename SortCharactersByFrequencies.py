from collections import Counter,OrderedDict
string="tree"
#counter map which creates a hash map as key character and value as frequency count of each character
mp=Counter(string)
print(mp)
#orderedDict--> trvasering through each items considering the key and value ordering the dict in 
#suppose map={'t':1,'r':1,'e':2}
#lambda function is used to get the value and ordering in reverse i.e in descending order of values
                                        # x-->  ( t,1)  to result the string in descending order
order=OrderedDict(sorted(mp.items(),key=lambda x:x[1],reverse=True))
print(order)
ss=''.join(char*fre for char,fre in order.items())
print(ss)
