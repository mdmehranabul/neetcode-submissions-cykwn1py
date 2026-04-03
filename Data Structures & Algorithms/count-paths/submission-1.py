class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # def dfs(r,c):
        #     if r>=m or c>=n: return 0
        #     if r == m-1 or c == n-1 : return 1

        #     return dfs(r,c+1) + dfs(r+1,c)
        
        # return dfs(0,0)

# Time Complexity - O(2^(m + n))
# Space Complexity - O(m + n)

        def dfs(r,c, cache):
            if (r,c) in cache: return cache[(r,c)]
            if r>=m or c>=n: return 0
            if r == m-1 or c == n-1 : return 1

            cache[(r,c)] = dfs(r,c+1,cache) + dfs(r+1,c,cache)
            return cache[(r,c)]
        
        return dfs(0,0,{})

# Time Complexity - O(m x n)
# Space Complexity - O(m x n)

        # dp =[[0]*(n) for _ in range(m)]

        # for i in range(m):
        #     for j in range(n):
        #         if (i == m-1 or j==n-1):
        #             dp[i][j]=1

        # for i in range(m-2,-1,-1):
        #     for j in range(n-2,-1,-1):
        #         dp[i][j]=dp[i+1][j]+dp[i][j+1]
        # return dp[0][0]

# Time Complexity - O(m x n)
# Space Complexity - O(m x n)

        # dp = [1] * n
        # print(dp)

        # for i in range(m-2,-1,-1):
        #     new_dp = [0]*n
        #     new_dp[n-1]=1
        #     for j in range(n-2,-1,-1):
        #         new_dp[j]=new_dp[j+1] + dp[j]
        #     dp=new_dp
        
        # return dp[0]

# Time Complexity - O(m x n)
# Space Complexity - O(n)


