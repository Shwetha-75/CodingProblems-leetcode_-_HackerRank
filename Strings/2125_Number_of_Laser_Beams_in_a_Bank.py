class Solution:
    def numberOfBeams(self, bank: list[str]) -> int: 
        hash_row={}
        row,col=len(bank),len(bank[0])
        for i in range(row):
            for j in range(col):
                print(bank[i][j])
                if bank[i][j]=='1':
                    if i not in hash_row:
                       hash_row[i]=1 
                    else:
                        hash_row[i]+=1 
        count=0 
        prev=-1
        for i in range(1,row):
            temp=i-1
            while temp!=-1:
                  if temp in hash_row and i in hash_row:
                     count+=hash_row[temp]*hash_row[i]
                     break
                  temp-=1 
        return count 
# Optimized 
class Solution:
      def numberOfBeams(self, bank: list[str]) -> int: 
        hash_row={}
        row,col=len(bank),len(bank[0])
        for i in range(row):
            for j in range(col):
                print(bank[i][j])
                if bank[i][j]=='1':
                    if i not in hash_row:
                       hash_row[i]=1 
                    else:
                        hash_row[i]+=1 
        count=0 
        print(hash_row)
        prev=0 if 0 in hash_row else -1 
        for i in range(1,row):
            if prev>=0 and prev in hash_row and i in hash_row and prev<i:
                count+=hash_row[i]*hash_row[prev]
                prev=i
            if i in hash_row:
                prev=i 
        return count

class TestApp:
      def testing_case_one(self):
          assert Solution().numberOfBeams(["011001","000000","010100","001000"])==8
      def testing_case_two(self):
          assert Solution().numberOfBeams(["000","111","000"])==0
      def testing_case_three(self):
          assert Solution().numberOfBeams(["00000","00101","10100","11110","11100","01001","00100","11010"])==35