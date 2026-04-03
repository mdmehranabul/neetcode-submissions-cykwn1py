class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit=set()

        adjlist={i:[] for i in range(n)}

        for n1,n2 in edges:
            adjlist[n1].append(n2)
            adjlist[n2].append(n1)

        def dfs(i,prev):
            if i in visit: return False
            visit.add(i)

            for j in adjlist[i]:
                if j==prev: continue
                if not dfs(j,i): return False
            
            return True
        
        return dfs(0,-1) and (n==len(visit))


        