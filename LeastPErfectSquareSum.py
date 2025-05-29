def findLeastPerfectSquare(num):
    #initialize array with [inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf]
    array=[float('inf')]*(num+1)
    # array=[inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf]
    array[0]=0
    count=1
    #outer loop
    
    while count*count<=num:
        perf=count*count#since the inner loop should start from perf
        for i in range(perf,num+1):
            array[i]=min(array[i-perf]+1,array[i])
            #count=1
            #       0 1 2 3 4 5 6 7 8 9 10 11 12
            #array=[0,1,2,3,4,5,6,7,8,9,10,11,12]
            #since every elements are summed up with 1--> perfect
            #count=2 count*count=4
            #how many elements require to add up with 4 to get min sum of elements
            #array[4]=min(array[4-4]+1,array[4])
            #         min(array[0]+1,4)-->min(1,4)--->array[4]=1
            #
            #
            # 0 1 2 3 4 5 6 7 8 9 10 11 12 
            #[0 1 2 3 1 2 3 4 2 3 4   5  3 ]
            #4-->4
            #5=4+1
            #6=4+1
            #7=4+1+1+1
            #8=4+4
            #9=4+4+1
            #....
            #perfect square 9 count=3 -->perf=9
            #  0 1 2 3 4 5 6 7 8 9 10 11  12 
            ##[0 1 2 3 1 2 3 4 2 3  4   5  3 ]-->prev
            # [0 1 2 3 1 2 3 4 2 1  2   3  3 ]-->updated-->12 9+1+1+1-->4,3
            #the iteration starts from 9
            
        count+=1
    return array[num]
print(findLeastPerfectSquare(12))
#12=4+4+4-->3
#13=4+9-->2