class Solution:
    def maxTaskAssign(self, tasks: list[int], workers: list[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        return max(self.maximumCheck(tasks[::],workers,pills,strength),self.minimumCheck(tasks[::],workers,pills,strength)) 
    def maximumCheck(self,tasks: list[int], workers: list[int], pills: int, strength: int):
        count=0
        index=len(workers)-1 
        while tasks and index>=0:
              task=tasks.pop(0)
              while index>=0:
                    if workers[index]>=task:
                       count+=1 
                       index-=1
                       break 
                    if workers[index]+strength>=task and pills:
                       count+=1 
                       index-=1 
                       pills-=1
                       break
                    index-=1 
        return count   
        
    def minimumCheck(self,tasks: list[int], workers: list[int], pills: int, strength: int):
        count=index=0 
        while tasks and index<len(workers):
              task=tasks.pop(0)
              while index<len(workers):
                    if workers[index]>=task:
                       count+=1 
                       index+=1
                       break 
                    if workers[index]+strength>=task and pills:
                       count+=1 
                       index+=1 
                       pills-=1
                       break 
                    index+=1 
        return count
        
class TestApp:
      def testing_case_one(self):
          assert Solution().maxTaskAssign([3,2,1],[0,3,3],1,1)==3 
      def testing_case_two(self):
          assert Solution().maxTaskAssign([5,4],[0,0,0],1,5)==1
      def testing_case_three(self):
          assert Solution().maxTaskAssign([10,15,30],[0,10,10,10,10],3,10)==2    
      def testing_case_four(self):
          assert Solution().maxTaskAssign([5,9,8,5,9],[1,6,4,2,6],1,5)==3