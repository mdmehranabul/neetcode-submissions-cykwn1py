class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # nums.sort() # 1,2,3
        # def dfs(total):
        #     if total == 0: return 1
        #     res = 0

        #     for i in range(len(nums)):
        #         if total < nums[i]:
        #             break
        #         res+=dfs(total - nums[i])
        #     return res

        # return dfs(target)

# Time Complexity - O(len(nums)^target)
# Space Complexity - O(target)

        # nums.sort() # 1,2,3
        # def dfs(total,cache):
        #     if total in cache: return cache[total]
        #     if total == 0: return 1
        #     res = 0

        #     for i in range(len(nums)):
        #         if total < nums[i]:
        #             break
        #         res+=dfs(total - nums[i],cache)
        #         cache[total]= res
        #     return res

        # return dfs(target,{})

# Time Complexity - O(len(nums) x target)
# Space Complexity - O(target)

        nums.sort()
        dp=[0]*(target + 1)
        dp[0]=1

        for total in range(1, target+1):
            for n in nums:
                if total < n:
                    break
                dp[total]+=dp[total-n]
        return dp[target]





