def numbers(left,right):
    '''#Approach 1
    ans=left
    for i in range(left+1,right+1):
        ans&=i
        
    print(ans)'''
    
    #Approach 2
    '''count=0
    while left!=right and left>0:
          count+=1
          left=left>>1
          right=right>>1
    return left<<count'''
    
    #Approach3 
    while right>left:
        right=right &right -1
    return left & right
left=11
right=13
print(numbers(left,right))