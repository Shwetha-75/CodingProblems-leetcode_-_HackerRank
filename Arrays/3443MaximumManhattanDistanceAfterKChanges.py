import sys
class Solution:
    
      def findDistanceNS(self,s):
          result=[[0,0]]
          max_distance_so_far=0
          minimum=sys.maxsize
          min_direction=''
          min_index=0
          max_index=0
          max_direction=''
          for i in range(len(s)):
              prev=result[-1]
              match(s[i]):
                  case 'N':
                      result.append([prev[0],prev[1]+1])
                  case 'S':
                      result.append([prev[0],prev[1]-1])
                  case 'E':
                      result.append([prev[0]+1,prev[1]])
                  case 'W':
                      result.append([prev[0]-1,prev[1]])
              current_sum=abs(result[-1][0])+abs(result[-1][1])
              if current_sum>max_distance_so_far and (s[i]=='N' or s[i]=='S'):
                  max_distance_so_far=current_sum 
                  max_direction=s[i]
                  max_index=i
              if current_sum<minimum and (s[i]=='N' or s[i]=='S'):
                  minimum=current_sum 
                  min_direction=s[i] 
                  min_index=i
          print("Result WE",result)
          return ((max_distance_so_far,max_direction,max_index),(minimum,min_direction,min_index))     
      def findDistanceWE(self,s):
          result=[[0,0]]
          max_distance_so_far=0
          minimum=float('-inf')
          min_direction=''
          max_direction=''
          max_index=0
          min_index=0
          for i in range(len(s)):
              prev=result[-1]
              match(s[i]):
                  case 'E':
                      result.append([prev[0]+1,prev[1]])
                  case 'W':
                      result.append([prev[0]-1,prev[1]])
                  case 'N':
                      result.append([prev[0],prev[1]+1])
                  case 'S':
                      result.append([prev[0],prev[1]-1])
              current_sum=abs(result[-1][0])+abs(result[-1][1])
              if current_sum>max_distance_so_far and (s[i]=='W' or s[i]=='E'):
                  max_distance_so_far=current_sum 
                  max_direction=s[i]
                  max_index=i
              if current_sum<minimum and (s[i]=='W' or s[i]=='E'):
                  minimum=current_sum 
                  min_direction=s[i] 
                  min_index=i
          print("Result NS: ",result)
          return ((max_distance_so_far,max_direction,max_index),(minimum,min_direction,min_index))     
      def maxDistance(self, s: str, k: int) -> int:
        #   finding the distance 
        s=list(s)
        resultNS=self.findDistanceNS(s)
        resultWE=self.findDistanceWE(s)
        print(resultNS,resultWE)
        max_distance=max(resultNS[0][0],resultWE[0][0])
        while k>0:
             if resultWE[1][0]<resultNS[1][0] and resultWE[1][1]!=resultWE[0][1]:
                temp=resultWE[1][2]
                s[temp]='E' if s[temp]=='W' else 'W'
                    
                temp_resultWE=self.findDistanceWE(s)
                k-=1
                if temp_resultWE[0][0]==max_distance:
                   s[temp]='E' if s[temp]=='W' else 'W'
                   k+=1
                   
                elif temp_resultWE[0][0]>max_distance:
                    max_distance=temp_resultWE[0][0]
                    resultWE=temp_resultWE
             elif resultNS[1][0]<resultWE[1][0] and resultNS[1][1]!=resultNS[0][1]:
                  temp=resultNS[1][2]
                  s[temp]='N' if s[temp]=='S' else 'S'
                  temp_resultNS=self.findDistanceNS(s)
                  k-=1
                  if temp_resultNS[0][0]==max_distance:
                      s[temp]='N' if s[temp]=='S' else 'S'
                      k+=1
                  elif temp_resultNS[0][0]>max_distance:
                      max_distance=temp_resultNS[0][0]
                      resultNS=temp_resultNS
             else:
                 break
             print(max_distance) 
        print(max_distance)
        return max_distance 
Solution().maxDistance("NWSE",1)

                  
                    
                
                 