'''
You are given an array arr, consisting of only zeroes, ones and twos.
Sort the same array in-place and return it. Do not create a new array.

Input:
n - the size of arr
arr - the array itself

Output:
A sorted array

Constraints:
1 <= n <= 100
0 <= arr[i] <= 2

SAMPLE INPUT 
5
2 0 1 0 2
SAMPLE OUTPUT 
0 0 1 2 2
Time Limit:	5.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB
Marking Scheme:	Score is assigned if any testcase passes.

'''

#method to perform the sorting
def sortItUp(array):
    #left pointer
    left=0
    #cur pointer
    cur=0
    #right pointer
    right=len(array)-1
    #as soon as we hit right it would break
    while cur<=right:
        #if we encounter 2
        #swap it with right index element
        if array[cur]==2:
            #swap
            array[cur],array[right]=array[right],array[cur]
            #decrement right
            right-=1
        #if we encounter 0
        #swap it with left index element
        if array[cur]==0:
            #swap
            array[cur],array[left]=array[left],array[cur]
            #increment cur as well as left
            cur+=1
            left+=1
        #if we encounter 1 
        #just increment cur
        if array[cur]==1:
            cur+=1
    return array
array=[2,0,1,0,2]
print(sortItUp(array))


# int the result [0,0,1,2,2]
# we can see the 0's are at the left most
# we can see the 2's are at the right most
# 0,0,|1|,2,2 1-->at th1 middle 
# we can create three pointers      #swap                    #swap          swap
#  left    right                   left    right             l     r       l   r               l r          l r         l r
#   |       |                        |       |               |     |       |   |               | |          | |         | |     
#  [2,0,1,0,2]   cur=0,l=0,r=0      [2,0,1,0,2]             [2,0,1,0,2]   [0,0,1,2,2]       [0,0,1,2,2]  [0,0,1,2,2] [0,0,1,2,2]
#   |                                |                       |             |                   |              |             |-->break
#  cur                               cur=2                   c=2           c=0                 c=0            c=1           c=1
# 
#
#what if this condition like c<=len(array) --> we can see in the above example r says that i have already stored 2 at the right most 
#by indicating one decremental so you cannot exculde r we can see arr[r]=1  arr[cur]=2 then it will perform swapping 
#the cur will not increment and we encounter infinite loop as well as right will be having negative indexing array out of bounds
#
#
#
#
#
#