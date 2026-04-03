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

        m,n = len(obstacleGrid), len(obstacleGrid[0])

        def dfs(r,c, cache):
            if (r,c) in cache: return cache[(r,c)]
            if r>=m or c>=n or obstacleGrid[r][c]:
                return 0   
            if r==m-1 and c==n-1 : return 1

            cache[(r,c)] = dfs(r+1,c, cache) + dfs(r,c+1, cache)
            return cache[(r,c)]
        return dfs(0,0,{})