class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # n = len(costs)

        # def dfs(i,prev):
        #     if i == n: return 0

        #     res= float("inf")
        #     for c in range(3):
        #         if c == prev:
        #             continue
                
        #         res = min(res, costs[i][c] + dfs(i+1,c))
        #     return res

        # return dfs(0,-1)

# Time Complexity - O(2^n)
# Space Complexity - O(n)

        # n = len(costs)

        # def dfs(i,prev,cache):
        #     if (i, prev) in cache: return cache[(i,prev)]
        #     if i == n: return 0

        #     res= float("inf")
        #     for c in range(3):
        #         if c == prev:
        #             continue
                
        #         res = min(res, costs[i][c] + dfs(i+1,c, cache))
        #         cache[(i,prev)] = res

        #     return res

        # return dfs(0,-1,{})

# Time Complexity - O(n)
# Space Complexity - O(n)

        # n = len(costs)

        # if n ==0 : return 0

        # dp = [[0] * 3 for i in range(n)]
        
        # dp[0] = costs[0]


        # for i in range(1, n):
        #     dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        #     dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        #     dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
        
        # return min(dp[n-1])

# Time Complexity - O(n)
# Space Complexity - O(n)

        n = len(costs)

        if n == 0 : return 0

        dp = costs[0]

        for i in range(1, n):
            dp0 = costs[i][0] + min(dp[1],dp[2])
            dp1 = costs[i][1] + min(dp[0],dp[2])
            dp2 = costs[i][2] + min(dp[0],dp[1])

            dp = [dp0, dp1, dp2]
        
        return min(dp)

# Time Complexity - O(n)
# Space Complexity - O(1)