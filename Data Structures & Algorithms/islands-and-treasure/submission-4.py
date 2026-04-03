class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows,cols=len(grid),len(grid[0])
        q=deque()
        visited=set()

        def add_dist(r,c):
            if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c]!=-1:
                visited.add((r,c))
                q.append((r,c))
            else: return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    visited.add((r,c))
                    q.append((r,c))

        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                add_dist(r+1,c)
                add_dist(r-1,c)
                add_dist(r,c+1)
                add_dist(r,c-1)
            dist+=1