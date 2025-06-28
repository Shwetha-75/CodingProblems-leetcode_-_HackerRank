

'''
#Previous Approach was partialy accepted
def jumpGame(array):
    jump=array[0]
    count=1
    i=0
    while i<=len(array)-1:
          if jump>=len(array):
              return count
          jump=array[i]
          i=jump+1
          count+=1
    print(count)
array=[3,1,2,1,7]
jumpGame(array)'''

def countMinimumJump(array):#      0 1 2 3 4
    target=len(array)-1#          [1,2,5,6,7]  -----> i=0,<4 t=4             , i=1,<4 t=4          ,i=2,<4 t=4
    count=0#                               |                0+1>=4-->false       1+1>=4-->false      2+5>=4-->true 
    while target!=0:#                     target=4                                                    t=2
        for i in range(target):#      0 1 2 3 4                                                            count=1
            if i+array[i]>=target:#  [1,2,5,6,7]  -----> i=0,<2                i=1,<2
                target=i#                 |               0+1>=2-->false      1+2>=2-->true
                break#                    target=2                              t=1
        count+=1#                      0 1 2 3 4                                count=2
    return count#                     [1,2,5,6,7]   ----->i=0,<1
  #                                      |                 0+1>=1-->true
  #                                    target=1            target=0
  #                                                      count=3
  #    target=0-->stopping condition
  #