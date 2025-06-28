from functools import reduce
import math
def superpower(a,b):
    b=int((''.join(map(str,b))))
    return pow(a,b,1337)
a=2147483647
b=[2,0,0]
print(superpower(a,b))

        