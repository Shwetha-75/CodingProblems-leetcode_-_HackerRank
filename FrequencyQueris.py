'''
You are given  queries. Each query is of the form two integers described below:
-  : Insert x in your data structure.
-  : Delete one occurence of y from your data structure, if present.
-  : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

The queries are given in the form of a 2-D array  of size  where  contains the operation, and  contains the data element.

Example

The results of each operation are:

Operation   Array   Output
(1,1)       [1]
(2,2)       [1]
(3,2)                   0
(1,1)       [1,1]
(1,1)       [1,1,1]
(2,1)       [1,1]
(3,2)                   1
Return an array with the output: .

Function Description

Complete the freqQuery function in the editor below.

freqQuery has the following parameter(s):

int queries[q][2]: a 2-d array of integers
Returns
- int[]: the results of queries of type 

Input Format

The first line contains of an integer , the number of queries.
Each of the next  lines contains two space-separated integers,  and .

Constraints

All 
Sample Input 0

8
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2
Sample Output 0

0
1
Explanation 0

For the first query of type , there is no integer whose frequency is  (). So answer is .
For the second query of type , there are two integers in  whose frequency is  (integers =  and ). So, the answer is .

Sample Input 1

4
3 4
2 1003
1 16
3 1
Sample Output 1

0
1
Explanation 1

For the first query of type , there is no integer of frequency . The answer is . For the second query of type , there is one integer,  of frequency  so the answer is .

Sample Input 2

10
1 3
2 3
3 2
1 4
1 5
1 5
1 4
3 2
2 4
3 2
Sample Output 2

0
1
1
'''

def findQuery(query):
    #result array
    array=[]
    dict1={}#insertion deletion updation on query
    for i in query:
        if i[0]==1:#insertion
            if i[1] not in dict1: dict1[i[1]]=1
            else: dict1[i[1]]+=1
        if i[0]==2:#deletion of frequency by 1 if key exists and value>0
            if i[1] in dict1: 
                if dict1[i[1]]>0:
                    dict1[i[1]]-=1
            
        if i[0]==3: #apppend 1 to array if frequency found in key or else 0 
            if i[1] in dict1.values():
                array.append(1)
            else: array.append(0)
    return array

def main():
    row=int(input())
    query=[]
    for i in range(row):
        temp=list(map(int,input().split()))
        
        query.append(temp)
    result=findQuery(query)
    print(result)
main()
        
        
            