class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        size = m * n
        par = [i for i in range(size)]
        rank = [1]*size
        islands=0
        visited=set()
        res = []

        def find(n1):
            res = n1

            while res != par[res]:
                par[res]=par[par[res]]
                res = par[res]
            return res
        
        def union(n1,n2):
            nonlocal islands
            p1,p2=find(n1), find(n2)
            if p1==p2:
                return False
            
            if rank[p1]>rank[p2]:
                rank[p1]+=rank[p2]
                par[p2]=p1
            else:
                rank[p2]+=rank[p1]
                par[p1]=p2
            islands-=1
            return True
        
        directions =[(0,1),(1,0),(0,-1),(-1,0)]

        for r,c in positions:
            idx = r*n+c

            if idx in visited:
                res.append(islands)
                continue
            
            visited.add(idx)
            islands+=1

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                nidx = nr*n + nc
                if 0<=nr<m and 0<=nc<n and nidx in visited:
                    union(idx, nidx)
            
            res.append(islands)
        return res


        