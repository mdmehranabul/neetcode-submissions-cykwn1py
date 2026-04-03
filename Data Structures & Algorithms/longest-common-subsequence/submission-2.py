class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # def dfs(i,j):
        #     if i==len(text1) or j==len(text2):
        #         return 0
            
        #     if text1[i]==text2[j]:
        #         return 1 + dfs(i+1,j+1)
            
        #     return max(dfs(i,j+1), dfs(i+1,j))
        # return dfs(0,0)

# Time Complexity : O(2^(m+n))
# Space Complexity : O(m+n)

        # def dfs(i,j, cache):
        #     if (i,j) in cache: return cache[(i,j)]
        #     if i==len(text1) or j==len(text2):
        #         return 0
            
        #     if text1[i]==text2[j]:
        #         cache[(i,j)] = 1 + dfs(i+1,j+1, cache)
        #         return cache[(i,j)]
            
        #     cache[(i,j)] = max(dfs(i,j+1,cache), dfs(i+1,j,cache))
        #     return cache[(i,j)]
        # return dfs(0,0, {})

# Time Complexity : O(m x n)
# Space Complexity : O(m x n)

        # dp = [[0]*(len(text2) + 1) for _ in range(len(text1)+1)]
        # for i in range(len(text1)-1,-1,-1):
        #     for j in range(len(text2)-1,-1,-1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i+1][j+1]
        #         else:
        #             dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        # return dp[0][0]

# Time Complexity : O(m x n)
# Space Complexity : O(m x n)

        M,N = len(text1),len(text2)
        dp = [0]*(N + 1)

        for i in range(M-1, -1, -1):
            newdp = [0]*(N + 1)
            for j in range(N-1, -1,-1):
                if text1[i] == text2[j]:
                    newdp[j] = 1 + dp[j+1]
                else:
                    newdp[j]=max(dp[j], newdp[j+1])
            dp = newdp
        return dp[0]

# Time Complexity : O(m x n)
# Space Complexity : O(n)