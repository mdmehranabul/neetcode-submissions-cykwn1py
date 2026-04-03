class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m,n = len(grid), len(grid[0])

        # def dfs(r,c):
        #     if r==m-1 and c==n-1: return grid[r][c]
        #     if r>=m or c>=n: return float("inf")

        #     return grid[r][c] + min(dfs(r+1,c), dfs(r,c+1))
        
        # return dfs(0,0)

# Time Complexity : O(2^(m+n))
# Space Complexity : O(m+n)
        # m,n = len(grid), len(grid[0])

        # def dfs(r,c,cache):
        #     if (r,c) in cache: return cache[(r,c)]
        #     if r==m-1 and c==n-1: return grid[r][c]
        #     if r>=m or c>=n: return float("inf")

        #     cache[(r,c)] = grid[r][c] + min(dfs(r+1,c,cache), dfs(r,c+1,cache))
        #     return cache[(r,c)]
        
        # return dfs(0,0,{})

# Time Complexity : O(m x n)
# Space Complexity : O(m x n)

        # m,n=len(grid),len(grid[0])
        # dp = [[float("inf")]*(n+1) for _ in range(m+1)]
        # dp[m][n-1]=0
        

        # for r in range(m-1,-1,-1):
        #     for c in range(n-1,-1,-1):
        #         dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])
        
        # return dp[0][0]

# Time Complexity : O(m x n)
# Space Complexity : O(m x n)

        # m,n=len(grid),len(grid[0])
        # dp = [[float("inf")]*(n+1) for _ in range(m+1)]
        # dp[m][n-1]=0
        

        # for r in range(m-1,-1,-1):
        #     for c in range(n-1,-1,-1):
        #         dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])
        
        # return dp[0][0]

# Time Complexity : O(m x n)
# Space Complexity : O(m x n)

        m,n=len(grid),len(grid[0])
        dp = [float("inf")]*(n+1)
        dp[n-1]=0
        print(dp)

        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                dp[c] = grid[r][c] + min(dp[c], dp[c+1])
        return dp[0]
        
# Time Complexity : O(m x n)
# Space Complexity : O(n)