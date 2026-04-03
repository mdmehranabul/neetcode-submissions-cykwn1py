class Solution:
    def climbStairs(self, n: int) -> int:

        # def dfs(i):
        #     if i<=1: return 1

        #     return dfs(i-1) + dfs(i-2)
        # return dfs(n)
    
    # Time Complexity : O(2^n)
    # Space Complexity : O(n)

        # def dfs(i, cache):
        #     if i in cache:
        #         return cache[i]
        #     if i<=1:
        #         return 1
            
        #     cache[i] = dfs(i-1, cache) + dfs(i-2, cache)
        #     return cache[i]
        # return dfs(n,{})
    
    # Time Complexity : O(n)
    # Space Complexity : O(n)

        dp=[0]*(n+1)
        dp[0],dp[1]=1,1

        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        
        return dp[n]





        