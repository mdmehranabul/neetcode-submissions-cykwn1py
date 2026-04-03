class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minHeap = [[grid[0][0],0,0]]

        directions =[[0,1],[0,-1],[1,0],[-1,0]]

        while minHeap:
            t,r,c = heapq.heappop(minHeap)

            if (r,c) ==(N-1,N-1): return t
            if (r,c) in visit: continue
            visit.add((r,c))

            for dr, dc in directions:
                neiR, neiC = dr+r, dc+c

                if (neiR<0 or neiC<0 or neiR==N or neiC==N or (neiR, neiC) in visit):
                    continue
                
                heapq.heappush(minHeap,[max(t,grid[neiR][neiC]),neiR, neiC])