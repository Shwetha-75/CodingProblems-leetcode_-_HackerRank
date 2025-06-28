class Solution:
    def findSolution(self, customfunction, z: int) ->list[list[int]]:
        result=[]
        for i in range(1,1000+1):
            x=i
            y=z-x 
            if customfunction(x,y)==z:
                result.append([x,y])
        return result 