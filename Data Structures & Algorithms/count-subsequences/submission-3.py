class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # def dfs(i1,i2):
        #     if i2==len(t): return 1
        #     if i1==len(s): return 0

        #     if s[i1]==t[i2]:
        #         return dfs(i1+1, i2+1) + dfs(i1+1,i2)
        #     else:
        #         return dfs(i1+1,i2)
        
        # return dfs(0,0)

# Time Complexity : O(2^m)
# Space Complexity : O(m)

        # def dfs(i1,i2,cache):
        #     if (i1,i2) in cache: cache[(i1,i2)]
        #     if i2==len(t):
        #         cache[(i1,i2)] = 1
        #         return cache[(i1,i2)]
        #     if i1==len(s):
        #         cache[(i1,i2)] = 0
        #         return cache[(i1,i2)]

        #     if s[i1]==t[i2]:
        #         cache[(i1,i2)] = dfs(i1+1, i2+1,cache) + dfs(i1+1,i2,cache)
        #         return cache[(i1,i2)]
        #     else:
        #         cache[(i1,i2)]= dfs(i1+1,i2,cache)
        #         return cache[(i1,i2)]
        
        # return dfs(0,0,{})

# Time Complexity : O(m)
# Space Complexity : O(m)

        # m,n = len(s), len(t)
        # dp =[[0]*(n+1) for _ in range(m+1)]

        # for i in range(m+1):
        #     dp[i][n]=1
        
        # for i in range(m-1,-1,-1):
        #     for j in range(n-1,-1,-1):
        #         if s[i]==t[j]:
        #             dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
        #         else:
        #             dp[i][j] = dp[i+1][j]
        # return dp[0][0]

# Time Complexity : O(m)
# Space Complexity : O(m)

        m,n = len(s), len(t)
        dp =[0]*(n+1)
        dp[n]=1
        
        for i in range(m-1,-1,-1):
            newdp=[0]*(n+1)
            newdp[n]=1
            for j in range(n-1,-1,-1):
                if s[i]==t[j]:
                    newdp[j] = dp[j+1] + dp[j]
                else:
                    newdp[j] = dp[j]
            dp = newdp
        return dp[0]

# Time Complexity : O(m)
# Space Complexity : O(1)