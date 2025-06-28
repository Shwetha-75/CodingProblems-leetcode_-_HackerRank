class Solution:
      def findHighAccessEmployees(self, access_times: list[list[str]]) -> list[str]:
          hash_map:dict={}
          for access in access_times:
              if access[0] in hash_map:
                  hash_map[access[0]].append(access[1])
              else:
                  hash_map[access[0]]=[access[1]]
          
          