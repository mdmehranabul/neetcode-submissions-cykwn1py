class Solution:
    def numDecodings(self, s: str) -> int:
        # def dfs(i):
        #     if i==len(s): return 1
        #     if s[i]=="0": return 0

        #     res=dfs(i+1)
        #     if i<len(s)-1:
        #         if (s[i]=="1" or (s[i]=="2" and s[i+1]<"7")):
        #             res+=dfs(i+2)            
        #     return res
        # return dfs(0)    

# Time Complexity - O(2^n)
# Space Complexity - O(n)

        # def dfs(i, cache):
        #     if i in cache:
        #         return cache[i]
            
        #     if i == len(s): return 1
        #     if s[i] == "0": return 0

        #     cache[i]=dfs(i+1,cache)
        #     if i <len(s)-1:
        #         if s[i]=="1" or (s[i]=="2" and s[i+1]<"7"):
        #             cache[i]+=dfs(i+2,cache)
        #     return cache[i]
        # return dfs(0,{})

# Time Complexity - O(n)
# Space Complexity - O(n)

        # n = len(s)
        # dp=[0]*(n+1)
        # dp[n]=1

        # for i in range(n-1,-1,-1):
        #     if s[i]=="0":
        #         dp[i]=0
        #     else:
        #         dp[i]=dp[i+1]
            
        #     if i < (n-1):
        #         if s[i]=="1" or (s[i]=="2" and s[i+1]<"7"):
        #             dp[i]+=dp[i+2]
        # return dp[0]

# Time Complexity - O(n)
# Space Complexity - O(n)

        dp1,dp2=1,0
        n = len(s)
        for i in range(n-1,-1,-1):
            if s[i]=="0":
                curr = 0
            else:
                curr = dp1

            if i < (n-1):
                if (s[i]=="1" or (s[i]=="2" and s[i+1] < "7")):
                    curr +=dp2
            
            dp2=dp1
            dp1=curr
        
        return dp1

# Time Complexity - O(n)
# Space Complexity - O(1)