class Solution:
    def minimumNumberUnique(self,array:list):
        numTracker=0
        minTracker=0
        for i in array:
            numTracker=max(i,numTracker)
            minTracker+=numTracker-i
            numTracker+=1
        return minTracker 
def main():
    sol=Solution()
    result=sol.minimumNumberUnique([1,2,2])
    print(result)
main()
            