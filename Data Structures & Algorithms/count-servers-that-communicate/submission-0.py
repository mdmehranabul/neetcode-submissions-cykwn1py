class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        ROW_CNT = [0]*ROWS
        COL_CNT = [0]*COLS

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    ROW_CNT[r]+=1
                    COL_CNT[c]+=1
        res=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and (ROW_CNT[r]>1 or COL_CNT[c]>1):
                    res+=1

        return res