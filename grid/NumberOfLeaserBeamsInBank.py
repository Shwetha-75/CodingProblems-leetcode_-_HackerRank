class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        count=[0]*len(bank)
        for i in range(len(bank)):
            count[i]=bank[i].count("1")
        total=0
        prev=count[0]
        for i in range(1,len(count)):
            total+=prev*count[i]
            prev=count[i] if count[i]>0 else prev 
            
        return total 
class TestApp:
      def testing_case_one(self):
          assert Solution().numberOfBeams(["011001","000000","010100","001000"])==8 
      def testing_case_two(self):
          assert Solution().numberOfBeams(["000","111","000"])==0