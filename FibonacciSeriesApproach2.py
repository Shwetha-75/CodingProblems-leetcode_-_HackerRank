class FibanocciSeries:
    def findFibo(n):#                                         O(n)                              f(5)          O(n)
        dict1={0:0,1:1}#                                                                      /      \
        if n not in dict1:#                                                             f(4)           f(3)
            dict1[n]=FibanocciSeries.findFibo(n-1)+FibanocciSeries.findFibo(n-2)#    /       \        /    \
            return dict1[n]#                                                    f(3)         f(2)    f(2)   f(1)
        else:#                                                                /      \     /    \    /   \  
            return dict1[n]#                                                f(2)   f(1) f(1)   f(0) f(1)  f(0)
n=6#                                                                       /    \
print(FibanocciSeries.findFibo(n))#                                    f(1)      f(0)