class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # if (len(s1) + len(s2))!=len(s3): return False

        # def dfs(i1,i2):
        #     if i1==len(s1) and  i2==len(s2) : return True

        #     if i1<len(s1) and s1[i1]==s3[i1+i2] and dfs(i1+1,i2): return True
        #     if i2<len(s2) and s2[i2]==s3[i1+i2] and dfs(i1,i2+1): return True
        #     return False
        
        # return dfs(0,0)

# Time Complexity : O(2^(m+n))
# Space Complexity : O(m+n)

        # if (len(s1) + len(s2))!=len(s3): return False

        # def dfs(i1,i2,cache):
        #     if (i1,i2) in cache:
        #         return cache[(i1,i2)]

        #     if i1==len(s1) and  i2==len(s2) :
        #         cache[(i1,i2)] = True
        #         return cache[(i1,i2)]

        #     if i1<len(s1) and s1[i1]==s3[i1+i2] and dfs(i1+1,i2,cache):
        #         cache[(i1,i2)] = True
        #         return cache[(i1,i2)]

        #     if i2<len(s2) and s2[i2]==s3[i1+i2] and dfs(i1,i2+1,cache):
        #         cache[(i1,i2)] = True
        #         return cache[(i1,i2)]

        #     cache[(i1,i2)] = False
        #     return cache[(i1,i2)]
        
        # return dfs(0,0,{})


# Time Complexity : O(m x n)
# Space Complexity : O(m x n)

        m,n = len(s1), len(s2)
        if m+n!= len(s3): return False
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[m][n] = True

        for i in range(m,-1,-1):
            for j in range(n,-1,-1):
                if i<m and s1[i]==s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j<n and s2[j]==s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True

        print(dp)
        return dp[0][0]


