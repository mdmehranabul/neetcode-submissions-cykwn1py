class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # def dfs(i):
        #     if i >=len(cost):
        #         return 0
            
        #     return cost[i] + min(dfs(i+1), dfs(i+2))
        # return min(dfs(0), dfs(1))
    
    # Time Complexity - O(2^n)
    # Space Complexity - O(n)

        # def dfs(i, cache):
        #     if i in cache:
        #         return cache[i]
            
        #     if i>= len(cost):
        #         return 0
            
        #     cache[i] = cost[i] + min(dfs(i+1,cache), dfs(i+2, cache))
        #     return cache[i]
        # return min(dfs(0,{}), dfs(1,{}))
    
    # Time Complexity - O(n)
    # Space Complexity - O(n)

        # dp=[0]*(len(cost))
        # dp[-1],dp[-2]=cost[-1], cost[-2]

        # for i in range(len(cost)-3,-1,-1):
        #     dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        # return min(dp[0],dp[1])

    # Time Complexity - O(n)
    # Space Complexity - O(n)


        # for i in range(len(cost)-3, -1, -1):
        #     cost[i]+=min(cost[i+1], cost[i+2])
        
        # return min(cost[0],cost[1])
    
    # Time Complexity - O(n)
    # Space Complexity - O(1)

        dp1, dp2= cost[-2], cost[-1]
        
        for i in range(len(cost)-3,-1,-1):
            dp1,dp2=cost[i]+min(dp1,dp2), dp1
        
        return min(dp1,dp2)