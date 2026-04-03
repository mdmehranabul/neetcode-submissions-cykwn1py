class Solution:
    def tribonacci(self, n: int) -> int:
        
        # def dfs(i):
        #     if i == 0: return 0
        #     if i <= 2 : return 1

        #     return dfs(i-1)+dfs(i-2)+dfs(i-3)
        
        # return dfs(n)

# Time Complexity - O(3^n)
# Space Complexity - O(n)

        # def dfs(i,cache):
        #     if i in cache: return cache[i]
        #     if i == 0: return 0
        #     if i <= 2 : return 1

        #     cache[i]=dfs(i-1,cache)+dfs(i-2,cache)+dfs(i-3,cache)
        #     return cache[i]
        
        # return dfs(n,{})
        
# Time Complexity - O(n)
# Space Complexity - O(n)

        dp=[0]*(n+1)
        if n==0: return 0
        if n<=2: return 1
        dp[1]=1
        dp[2]=1

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        return dp[n]

# Time Complexity - O(n)
# Space Complexity - O(n)

        # if n==0: return 0
        # if n<=2: return 1
        # dp0,dp1,dp2=0,1,1

        # for i in range(3,n+1):
        #     dp2,dp1,dp0= dp0+dp1+dp2, dp2, dp1
        
        # return dp2

# Time Complexity - O(n)
# Space Complexity - O(1)