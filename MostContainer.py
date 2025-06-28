class Container:
    def findingArea(array):
        maxArea=0
        for i in range(len(array)-1):
            area=0
            for j in range(i,len(array)):
                area=min(array[i],array[j])*(j-i)
                if maxArea<area:
                    maxArea=area  
        return maxArea
array=[1,5,6,3,4]
print(Container.findingArea(array))