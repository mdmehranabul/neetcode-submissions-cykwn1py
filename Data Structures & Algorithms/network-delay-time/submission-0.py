class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges=defaultdict(list)
        res=0
        visit=set()
        minH=[[0,k]] # initial distance is assumed to be 0

        for u,v,w in times:
            edges[u].append([v,w])
        
        while minH:
            dist,node=heapq.heappop(minH)
            if node in visit:
                continue
            visit.add(node)
            res=max(res,dist)

            for node_neigh,node_dist in edges[node]:
                if node_neigh not in visit:
                    heapq.heappush(minH,[node_dist+dist,node_neigh])

        return res if n==len(visit) else -1


        
        