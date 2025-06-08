class UnionFind:
      def __init__(self,size):
          self.parent=list(range(size))
      def find(self,i):
          if self.parent[i]==i:
              return i 
          return self.find(self.parent[i])
      def union(self,i,j):
          left=self.find(i)
          right=self.find(j)
          self.parent[left]=right 

size=5
unionFind=UnionFind(size)
unionFind.union(1,2)
unionFind.union(3,4)
print("Are 1 is parent of 2 ",unionFind.find(1)==unionFind.find(2))
print("Are 3 is parent of 4 ",unionFind.find(3)==unionFind.find(4))
unionFind.union(0,3)
print("Are 0 is parent of 3 ",unionFind.find(0)==unionFind.find(4))
print(unionFind.parent)