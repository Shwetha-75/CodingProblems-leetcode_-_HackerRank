#Using Floyd's tortoise and hare algorithm
def dupliacte(nums):
    tortoise=0
    hare=0
    #we will run the loop until the hare and tortoise will meet
    #since the given array as one duplicate element
    while True:
        #hare will be moving two steps a head
        hare=nums[nums[hare]]
        #tortoise will be moving one step a head   tortoise and hare will point at elements not indexes
        tortoise=nums[tortoise]    #                     0 1 2 3 4 5 6 7              
        #if elements are matching in the           nums=[1,2,3,4,5,6,3,7]  when we create a linked list
        if hare==tortoise:#                                  |       |
            ptr=0#                                        tortoise
            while ptr!=tortoise:#                                       1->2->3->4->5->6
                ptr=nums[ptr]#                                                |________|
                tortoise=nums[tortoise]#
            return ptr#
nums=[1,2,3,4,5,6,3,7]#

print(dupliacte(nums))
        