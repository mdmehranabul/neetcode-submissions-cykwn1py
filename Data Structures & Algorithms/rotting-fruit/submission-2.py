class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh, time = 0,0
        q=deque()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh+=1
        
        while q and fresh:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c]==1:
                        q.append((r,c))
                        grid[r][c]=2
                        fresh-=1
            time+=1
        
        return time if not fresh else -1


        