class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [1]*n
        self.count = n
    
    def find(self,x):

        while x!=self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x=self.par[x]
        return x
    
    def union(self,x1,x2):
        p1,p2 = self.find(x1),self.find(x2)

        if p1==p2:
            return False
        
        if self.rank[p1]>self.rank[p2]:
            self.par[p2]=p1
            self.rank[p1]+=self.rank[p2]

        else :
            self.par[p1]=p2
            self.rank[p2]+=self.rank[p1]
        
        self.count-=1
        return True
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]:
                    uf.union(i,j)
        return uf.count

# Time Complexity - O(n^2)
# Space Complexity - O(n)