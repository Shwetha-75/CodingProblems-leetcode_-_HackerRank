from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        result=[]
        hash_map={}
        visited=defaultdict(int)
        for i in range(len(transactions)):
            # [name,time,amt,city]
            temp=transactions[i].split(",")
            temp[1]=int(temp[1])
            temp[2]=int(temp[2])
            
            # [name,time,amt,city]
            #   0     1    2    3  
            
            if temp[2]>1000:
                result.append(transactions[i])
            elif temp[0] in hash_map:
                 before=hash_map[temp[0]] 
                 flag=False
                 for j in range(len(before)):
                    #  print(before[j],temp)
                     if before[j]!=-1:
                        if before[j][3]!=temp[3] or (temp[1]-before[j][1]<=60 and temp[1]-before[j][1]>0):
                           if j not in visited: 
                              result.append(",".join(list(map(str,before[j]))))
                           before[j]=-1
                           visited[j]+=1
                           flag=True
                 hash_map[temp[0]].append(temp)
                 if flag:
                     result.append(",".join(list(map(str,temp))))
                     visited[len(hash_map[temp[0]])-1]+=1
                #  print("hash_map: ",hash_map[temp[0]])
                #  print("visited: ",visited)
                #  print("result: ",result)
            else:
                hash_map[temp[0]]=[temp]
            
        # print(hash_map)
        # print(result)
        # print(len(["alice,20,800,mtv",
        #            "bob,50,1200,mtv",
        #            "alice,20,800,mtv",
        #            "alice,50,1200,mtv",
        #            "alice,20,800,mtv",
        #            "alice,50,100,beijing"]))
        # print(len(result))
        # print(len(["alice,20,800,mtv","bob,50,1200,mtv","alice,20,800,mtv","alice,50,1200,mtv","alice,20,800,mtv","alice,50,100,beijing"])==len(result))
        # print(result)
        return result 
class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        result=[]
        hash_map={}
        visited=defaultdict(int)
        for i in range(len(transactions)):
            temp=transactions[i].split(",")
            temp[1]=int(temp[1])
            temp[2]=int(temp[2])
            temp=[i]+temp 
            if temp[3]>1000:
               result.append(transactions[i])
               visited[i]+=1
            if temp[1] in hash_map:
                hash_map[temp[1]].append(temp)
                res=self.checkTransaction(hash_map[temp[1]],visited,temp,result)
                if res and temp[0] not in visited:
                   result.append(",".join(list(map(str,temp[1::]))))
                   visited[i]+=1
            else:
                hash_map[temp[1]]=[temp]
        # print(result)
        return result            
                
                 
    def checkTransaction(self,list_transactions,visited,current,result):
        flag=False 
        for j in range(len(list_transactions)):
            # print(list_transactions)
            if list_transactions[j]!=-1:
               if list_transactions[j][4]!=current[4] and abs(list_transactions[j][2]-current[2])<=60:
                  if list_transactions[j][0] not in visited:
                     result.append(",".join(list(map(str,list_transactions[j][1::]))))
                  list_transactions[j]=-1
                  visited[j]+=1
                  flag=True
        return flag
                
Solution().invalidTransactions(["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"])
Solution().invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"])
Solution().invalidTransactions(["alice,20,800,mtv","alice,50,1200,mtv"])
Solution().invalidTransactions(["alice,20,800,mtv","bob,50,1200,mtv"])
Solution().invalidTransactions(["alice,20,800,mtv",
"bob,50,1200,mtv",
"alice,20,800,mtv",
"alice,50,1200,mtv",
"alice,20,800,mtv",
"alice,50,100,beijing"])


# ["alice,20,800,mtv","bob,50,1200,mtv","alice,20,800,mtv","alice,50,1200,mtv","alice,20,800,mtv","alice,50,100,beijing"]
class TestApp:
      def testing_case_one(self):
          assert Solution().invalidTransactions(["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"])