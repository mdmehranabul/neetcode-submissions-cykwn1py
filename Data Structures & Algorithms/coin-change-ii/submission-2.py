class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # def dfs(i, total):
        #     if i == len(coins): return 0
        #     if total == amount: return 1
        #     if total > amount: return 0

        #     return dfs(i, total+coins[i]) + dfs(i+1, total)
        # return dfs(0,0)

# Time Complexity : O(m^n)
# Space Complexity : O(m+n)

        # def dfs(i, total,cache):
        #     if (i,total) in cache: return cache[(i,total)]
        #     if i == len(coins): return 0
        #     if total == amount: return 1
        #     if total > amount: return 0

        #     cache[(i,total)] = dfs(i, total+coins[i],cache) + dfs(i+1, total,cache)
        #     return cache[(i,total)]
        # return dfs(0,0,{})

# Time Complexity : O(m x n)
# Space Complexity : O(m x n)

        # coins.sort()
        # n = len(coins)

        # dp = [[0]*(amount+1) for _ in range(n+1)]

        # for i in range(n+1):
        #     dp[i][0]=1
        
        # for i in range(1, n+1):
        #     for a in range(1, amount+1):
        #         dp[i][a] = dp[i-1][a]
        #         if a>=coins[i-1]:
        #             dp[i][a]+=dp[i][a-coins[i-1]]
        # return dp[n][amount]

# Time Complexity : O(m x n)
# Space Complexity : O(m x n)

        coins.sort()
        n = len(coins)

        dp = [0]*(amount+1)
        dp[0]=1

        for i in range(1, n+1):
            newdp=[0]*(amount+1)
            newdp[0]=1
            for a in range(1, amount+1):
                newdp[a]=dp[a]
                if a>=coins[i-1]:
                    newdp[a]+=newdp[a-coins[i-1]]
            dp=newdp
        
        return dp[amount]

# Time Complexity : O(m x n)
# Space Complexity : O(m)