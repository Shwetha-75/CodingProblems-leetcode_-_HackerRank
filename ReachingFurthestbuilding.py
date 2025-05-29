import heapq
import sys
def reachingFurthestBuilding(nums,bricks,ladder):
    '''jumps=0
    index=0
    for i in range(0,len(nums)-1):
        if nums[i]<nums[i+1]:
            temp=abs(nums[i]-nums[i+1])
            if ladder>0 or bricks>0:   
                if bricks>=temp:
                   bricks-=temp
                   index=i+1
                   jumps+=1
                else:
                   if ladder>0:
                      ladder-=1
                      index=i+1
                      jumps+=1
        else:
              print(nums[i],nums[i+1],i,i+1,index)
              if index==i:
                 index=i+1
                 jumps+=1
              else:
                  break
    return index'''
    
    heap=[]
    for i in range(0,len(nums)-1):
        temp=nums[i+1]-nums[i]
        if temp>0:
            heapq.heappush(heap,temp)
        if len(heap)>ladder:
            bricks-=heapq.heappop(heap)
            if bricks<0: 
                return i
    return len(nums)-1
nums=[4,2,7,6,9,14,12]
bricks=5
ladder=1
print(reachingFurthestBuilding(nums,bricks,ladder))