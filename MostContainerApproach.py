class MaxArea:
    #method to find maximum area
    def findingArea(array):
        #var declaration
        maxArea=0
        #letft pointer
        left=0
        #right pointer
        right=len(array)-1
        #stopping condition
        while left<right:
            #area=min(array[left],array[right])*(j-i)
            #finding the min between two arrays
            height=min(array[left],array[right])
            #finding the width difference of indexes
            width=right-left
            #max area 
            maxArea=max(maxArea,height*width)
            #shifying the pointers according to min element
            if array[left]<array[right]:left+=1
            else: right-=1
        return maxArea
array=[3,7,5,6,8,4]
print(MaxArea.findingArea(array))