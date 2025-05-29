class Solution:
      def largestTimeFromDigits(self, arr: list[int]) -> str:
        hours=0 
        stack=[] 
        for i in range(len(arr)):
            for j in range(len(arr)):
                temp=arr[i]*10+arr[j]
                if arr[i]*10+arr[j]<=23 and temp > hours and i!=j:
                    stack=[arr[i],arr[j]]
                    hours=temp 
    
        if hours<10:
            hours="0"+str(hours)
        hours=str(hours)
        if stack:
        
            arr.remove(stack[0])
            arr.remove(stack[1])
           
            minutes=arr[0]*10+arr[1] if arr[0]*10+arr[1]>arr[1]*10+arr[0] and arr[0]*10+arr[1]<=59  else arr[1]*10+arr[0]
            if minutes<10:
                return hours+":"+"0"+str(minutes)
            else:
                if minutes<=59:
                   return hours+":"+str(minutes)
                else:return ""
        else:
            return "00:00" if arr.count(0)==4 else ""
class TestApp:
      def testing_case_one(self):
          assert Solution().largestTimeFromDigits([1,2,3,4])=="23:41"
      def testing_case_two(self):
          assert Solution().largestTimeFromDigits([5,5,5,5])==""
      def testing_case_three(self):
          assert Solution().largestTimeFromDigits([0,0,1,0])=='10:00'