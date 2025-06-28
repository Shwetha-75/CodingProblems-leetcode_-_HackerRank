class Solution:
      def findSuperSetAndSubset(self,superset:str,subset:str):
          count=0
          if subset in superset:
              count+=superset.count(subset)
          temp=0
          for i in superset:
              if i=='?':
                  temp+=1
          