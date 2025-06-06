class Solution:
      def nextCells(self,cells:list[int])->list[int]:
          new_cells=[0]*8
          for i in range(1,7):
              new_cells[i]=int(cells[i-1]==cells[i+1])
          return new_cells
      def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
          hash_map={}
          for i in range(n):
            #   detect the loop
               temp=str(cells)
               if temp in hash_map:
                  loop_len=i-hash_map[temp]
                  return self.prisonAfterNDays(cells,(n-i)%loop_len)
               else:
                   hash_map[temp]=i 
                   cells=self.nextCells(cells)
          return cells 
class TestApp:
      def testing_case_one(self):
          assert Solution().prisonAfterNDays([0,1,0,1,1,0,0,1],7)==[0,0,1,1,0,0,0,0]
      def testing_case_two(self):
          assert Solution().prisonAfterNDays([1,0,0,1,0,0,1,0],1000000000)==[0,0,1,1,1,1,1,0]