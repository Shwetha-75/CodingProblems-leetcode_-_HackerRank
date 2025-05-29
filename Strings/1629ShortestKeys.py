class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        max_duration=releaseTimes[0]
        value=keysPressed[0]
        for i in range(1,len(releaseTimes)):
            if releaseTimes[i]-releaseTimes[i-1]>max_duration:
                max_duration=releaseTimes[i]-releaseTimes[i-1]
                value=keysPressed[i]
            elif releaseTimes[i]-releaseTimes[i-1]==max_duration and value<keysPressed[i]:
                 value=keysPressed[i]
        
        return value
class TestApp:
      def testing_case_one(self):
          assert Solution().slowestKey([9,29,49,50],"cbcd")=="c"
      def testing_casE_two(self):
          assert Solution().slowestKey([12,23,36,46,62],"spuda")=="a"