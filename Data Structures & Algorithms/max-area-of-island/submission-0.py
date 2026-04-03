class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visited=set()

        def dfs(r,c):

            if r in range(rows) and c in range(cols) and grid[r][c]==1 and ((r,c)) not in visited:
                visited.add((r,c))
                return (1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
            else: return 0
        maxarea=0
        for r in range(rows):
            for c in range(cols):
                maxarea=max(maxarea,dfs(r,c))
        return maxarea

