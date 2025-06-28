'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n

'''

#Problem Explaination
#we are given 2D matrix 
#we have to find the town judge person
#town judge is a person who is ---> trusted by himself and every one range from 1 to n-1 trust town judge person
#Eg. 
# persons a1,a2,a3,a4,a5
#  relation ship a1-->a2, a3-->a2, a4-->a2, a5-->a2  
# which means a2 is the town judge person 
#Suppose we have a1,a2,a3,a4,a5
#    relationships : a1-->a2,a2-->a3,a4-->a2,a5-->a2,a3-->a2
# in the above case ----> a2 is trusting a3 which should not be the case 
# so we return -1 since not other persons are in which every one trust him

def findTownJudgePerson(nums,n):
    #Observations
    #if the length of the 2D matrix is 0  and n==1 which means one person who only trust him
    if len(nums)==0 and n==1: return 1
    #if the length of th2e 2D matrix is 1 and n==2 which means at nums[0][1] is ths positon where townJudge person exists
    if len(nums)==1 and n==2: return nums[0][1]
    
    
    #reating hash map
    dict1={}
    #traverse thorugh 2D matrix to fing every possible town judge and their frequencies
    for i in nums:
        if i[1] not in dict1:
            dict1[i[1]]=1
        else:
            dict1[i[1]]+=1
    #we have to find that i the keys of dict(town judge person) who is trusting any one
    #if means we make the frequency to 0
    for i in nums:
        if i[0] in dict1:
            dict1[i[0]]=0
    #we find the town judge
    
    maxLen=0
    townJudge=0
    for i in dict1:
        #ensuring that frequency should be > 1
        if dict1[i]>1:
            #frequcny count
            #previous and present
            #Advancing the town Judge and maxLen
            if maxLen<dict1[i]:
                maxLen=dict1[i]
                townJudge=i
    #return only if the townJudge is updated and if the townJdge frequency is n-1
    #means every body trusts him
    #else -1 means no town judge 
    return townJudge if townJudge!=0 and dict1[townJudge]==n-1 else -1

nums= [[1,3],[2,3]]
n=3
value=findTownJudgePerson(nums,n)
print(value)       
                     