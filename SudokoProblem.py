def is_valid(arr):
    row=[[0 for i in range(9)] for j in range(9)]
    col=[[0 for i in range(9)] for j in range(9)]
    box=[[0 for i in range(9)] for j in range(9)]
    
    for i in range(9):
        for j in range(9):
            if arr[i][j]!=-1:
                value=arr[i][j]-1
                boxNo=3*(i//3)+j//3
                if col[j][value]==1 or box[boxNo][value]==1 or row[i][value]==1:
                    return 0
                else:
                    col[j][value]=1
                    row[i][value]=1
                    box[boxNo][value]=1
    return 1
    

arr = [[1,-1,-1,-1,2,-1,-1,-1,-1,3],
       [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1,1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [8,-1,-1,-1,-1,-1,-1,-1,-1,4],
       [9,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

out_ = is_valid(arr)
print (out_)