class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # m,n = len(obstacleGrid), len(obstacleGrid[0])

        # def dfs(r,c):
        #     if r>=m or c>=n or obstacleGrid[r][c]:
        #         return 0   
        #     if r==m-1 and c==n-1 : return 1

        #     return dfs(r+1,c) + dfs(r,c+1)
        # return dfs(0,0)

# Time Complexity : O(2^(m+n))
# Space Complexity : O(m+n)

        # m,n = len(obstacleGrid), len(obstacleGrid[0])

        # def dfs(r,c, cache):
        #     if (r,c) in cache: return cache[(r,c)]
        #     if r>=m or c>=n or obstacleGrid[r][c]:
        #         return 0   
        #     if r==m-1 and c==n-1 : return 1

        #     cache[(r,c)] = dfs(r+1,c, cache) + dfs(r,c+1, cache)
        #     return cache[(r,c)]
        # return dfs(0,0,{})

# Time Complexity : O(m x n)
# Space Complexity : O(m x n)

        m,n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] or obstacleGrid[m-1][n-1] : return 0

        dp = [[0]*n for _ in range(m)]
        dp[m-1][n-1] = 1

        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if obstacleGrid[r][c]:
                    dp[r][c]=0
                else:
                    if r+1<m:
                        dp[r][c]+= dp[r+1][c]
                    if c+1<n:
                        dp[r][c]+= dp[r][c+1]
        
        return dp[0][0]

# Time Complexity : O(m x n)
# Space Complexity : O(m x n)