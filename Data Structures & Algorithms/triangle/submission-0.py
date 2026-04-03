class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # N = len(triangle)

        # def dfs(row, col):
        #     if row == N: return 0

        #     return triangle[row][col]+min(dfs(row+1,col), dfs(row+1,col+1))
        # return dfs(0,0)

# Time Complexity : O(2^n)
# Space Complexity : O(n)

        # N = len(triangle)

        # def dfs(row, col, cache):
        #     if (row, col) in cache: return cache[(row, col)]
        #     if row == N : return 0

        #     cache[(row,col)] = triangle[row][col] + min(dfs(row+1, col, cache), dfs(row+1,col+1, cache))

        #     return cache[(row,col)]
        # return dfs(0,0,{})

# Time Complexity : O(n^2)
# Space Complexity : O(n^2)

        # N = len(triangle)
        # dp = [0]*(N+1)

        # for row in triangle[::-1]:
        #     for i, n in enumerate(row):
        #         dp[i]=n+min(dp[i], dp[i+1])
        
        # return dp[0]

# Time Complexity : O(n^2)
# Space Complexity : O(n^2)

        N = len(triangle)

        for row in range(len(triangle)-2,-1,-1):
            for col in range(len(triangle[row])):
                triangle[row][col]+=min(triangle[row+1][col], triangle[row+1][col+1])
        
        return triangle[0][0]

# Time Complexity : O(n^2)
# Space Complexity : O(1)