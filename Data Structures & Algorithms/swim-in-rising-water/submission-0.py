class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N=len(grid)
        time=0
        minH=[[grid[0][0],0,0]]
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        visit=set()
        while minH:
            time,r,c = heapq.heappop(minH)
            if r==N-1 and c==N-1: return time

            for dr,dc in directions:
                neigh_row,neigh_col=r+dr,c+dc
                if neigh_row in range(N) and neigh_col in range(N) and (neigh_row,neigh_col) not in visit:
                    heapq.heappush(minH,[max(grid[neigh_row][neigh_col],time),neigh_row,neigh_col])
                    visit.add((neigh_row,neigh_col))


        