class NonRepeating:
    def checkNonRepeating(self,string):
        list1=list(string)
        print(list1)
        for i,el in enumerate(list1):
            if list1.count(el)==1:
                return i
        
n=NonRepeating()
print(n.checkNonRepeating("aa@1234bcd"))    

            