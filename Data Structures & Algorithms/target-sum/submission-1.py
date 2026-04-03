class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # def dfs(i, total):
        #     if i == len(nums)  :
        #         return total == target
            
        #     return dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i])
        # return dfs(0,0)

# Time Complexity - O(2^n)
# Space Complexity - O(n)
        
        # def dfs(i, total,cache):
        #     if (i,total) in cache: return cache[(i,total)]
        #     if i == len(nums):
        #         return total == target
                
        #     cache[(i,total)]= dfs(i+1, total+nums[i],cache) + dfs(i+1, total-nums[i],cache)
        #     return cache[(i,total)]
        # return dfs(0,0,{})

# Time Complexity - O(m x n)
# Space Complexity - O(m x n)

        # n = len(nums)
        # offset = sum(nums)
        # dp = [[0]*(2*offset+1) for _ in range(n+1)]

        # dp[0][offset] = 1

        # for i in range(n):
        #     for j in range(-offset, offset+1):
        #         if dp[i][j+offset]:
        #             dp[i+1][j+offset+nums[i]]+=dp[i][j+offset]
        #             dp[i+1][j+offset-nums[i]]+=dp[i][j+offset]
        # print(dp)
        # return dp[n][offset+target] if -offset<=target<=offset else 0

# Time Complexity - O(m x n)
# Space Complexity - O(m x n)

        n = len(nums)
        offset = sum(nums)
        dp = [0]*(2*offset+1)

        dp[offset] = 1

        for i in range(n):
            newdp = [0]*(2*offset+1)
            for j in range(-offset, offset+1):
                if dp[j+offset]:
                    newdp[j+offset+nums[i]]+=dp[j+offset]
                    newdp[j+offset-nums[i]]+=dp[j+offset]
            dp=newdp
        return dp[offset+target] if -offset<=target<=offset else 0

# Time Complexity - O(m x n)
# Space Complexity - O(m)