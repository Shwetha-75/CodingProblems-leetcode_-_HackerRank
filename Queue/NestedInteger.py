class NestedInteger:
   def __init__(self,integer:int=None,list:list=[]):
       self._integer=integer 
       self._list=list 
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """
       
       return self._integer!=None
    

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """
       return self._integer
       

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer"""
       return self._list
       
   def to_dict(self):
       return {
           "_integer":self._integer,
           "_list":self._list
       }