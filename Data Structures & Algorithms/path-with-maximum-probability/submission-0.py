class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {i:[] for i in range(n)}

        for i in range(len(edges)):
            n1,n2 = edges[i]
            adj[n1].append([succProb[i],n2])
            adj[n2].append([succProb[i],n1])

        visit=set()
        minHeap = [(-1, start_node)]

        while minHeap:
            p1,n1 = heapq.heappop(minHeap)

            if n1==end_node:
                return -p1
            
            if n1 in visit:
                continue
            
            visit.add(n1)
            
            for p2,n2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (p1*p2, n2)) 
        
        return 0
        