class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        temp_left=list(dominoes)
        # left traversal 
        flag_left=False 
        for i in range(len(temp_left)-1,-1,-1):
            if temp_left[i]=='L':
               flag_left=True 
            if temp_left[i]=='.' and flag_left:
                temp_left[i]='L'
            if temp_left[i]=='R':
                flag_left=False 
        temp_right=list(dominoes)
        flag_right=False
        for i in range(len(dominoes)):
            if temp_right[i]=='R':
                flag_right=True 
            if temp_right[i]=='.' and flag_right:
                temp_right[i]='R'
            if temp_right[i]=='L':
                flag_right=False 
        count=index=0
        while index<len(temp_left):
            if temp_left[index]=='L' and temp_right[index]=='.':
               temp_right[index]='L'
            elif temp_right[index]=='R' and temp_left[index]=='L':
                start=index
                while temp_left[index]!=temp_right[index]:
                      count+=1
                      index+=1 
                if (index-start)% 2:
                    mid=(index+start)//2 
                    temp_right[mid]='.'
                    mid_r=mid+1 
                    while mid_r <index:
                         temp_right[mid_r]='L'
                         mid_r+=1 
                else:
                    mid=(start+index)//2 
                    while mid<index:
                          temp_right[mid]='L'
                          mid+=1 
                count=0 
            else:
                index+=1
        return "".join(temp_right)  
                     
class TestApp:
      def testing_case_one(self):
          assert Solution().pushDominoes("RR.L")=="RR.L"
      def testing_case_two(self):
          assert Solution().pushDominoes(".L.R...LR..L..")=="LL.RR.LLRRLL.."
      def testing_case_three(self):
          assert Solution().pushDominoes("RR.LL")=="RR.LL"    
      def testing_case_four(self):
          assert Solution().pushDominoes("RRRR....LLLL")=="RRRRRRLLLLLL"
        