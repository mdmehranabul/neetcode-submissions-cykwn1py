class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return False

        adjlist = {i:[] for i in range(n)}
        visit=set()
        for node1, node2 in edges:
            adjlist[node1].append(node2)
            adjlist[node2].append(node1)
        
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for j in adjlist[i]:
                if j==prev:
                    continue
                if not dfs(j,i):
                    return False
            return True

        return dfs(0,-1) and n == len(visit)
        