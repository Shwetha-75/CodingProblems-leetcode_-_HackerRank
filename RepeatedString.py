'''
There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer, , find and print the number of letter a's in the first  letters of the infinite string.

Example


The substring we consider is , the first  characters of the infinite string. There are  occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Returns

int: the frequency of a in the substring
Input Format

The first line contains a single string, .
The second line contains an integer, .

Constraints

For  of the test cases, .
Sample Input

Sample Input 0

aba
10
Sample Output 0

7
Explanation 0
The first  letters of the infinite string are abaabaabaa. Because there are  a's, we return .

Sample Input 1

a
1000000000000
Sample Output 1

1000000000000
Explanation 1
Because all of the first  letters of the infinite string are a, we return 
'''
def repeatedString(string,n):
    #Approach 1 Hacker Rank problem
    #Failed 15 test cases out of 25 
    #Runtim error Logic is wrong
    '''list1=list(string)
    if 'a' not in string: return 0
    j=0
    for i in range(len(string),n):
        if j==len(string):j=0
        list1.append(string[j])
        j+=1
   
    return list1.count('a')'''
    
    #Approach 2
    quo,rem=divmod(n,len(string))
    count=quo*string.count('a')
    if rem>0: count+=string[:rem:].count('a')
    return count
    
string='aba'
n=10
print(repeatedString(string,n))