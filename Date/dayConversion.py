class Solution:
    def convertingDay(self,y:int,m:int,d:int)->str:
        if m<3:
            m+=12
            y-=1 
        k=y%100
        j=y//100 
        days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        return days[(d+13*(m+1)//5+k+k//4+j//4+5*j)%7-1]
class TestApp:
    def testing_case_one(self):
        assert Solution().convertingDay(2019,5,16)=="Thursday"
    def testing_case_two(self):
        assert Solution().convertingDay(2020,10,29)=="Thursday"
    def testing_case_three(self):
        assert Solution().convertingDay(2017,5,21)=="Sunday"