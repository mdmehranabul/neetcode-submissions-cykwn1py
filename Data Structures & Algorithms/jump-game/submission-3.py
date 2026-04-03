class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # goal = len(nums)-1

        # for i in range(len(nums)-1,-1,-1):
        #     if i + nums[i]>=goal:
        #         goal = i
        
        # return True if goal == 0 else False

# Time Complexity - O(n)
# Space Complexity - O(1)
        n=len(nums)
        dp =[False]*n
        dp[-1]=True

        for i in range(n-2,-1,-1):
            end = min(n, i + nums[i]+1)
            for j in range(i+1,end):
                if dp[j]:
                    dp[i]=True
                    break
        return dp[0]

# Time Complexity - O(n^2)
# Space Complexity - O(n)