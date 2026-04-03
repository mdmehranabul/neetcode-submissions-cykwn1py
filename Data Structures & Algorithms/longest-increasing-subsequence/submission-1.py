class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(i, prev):
            if i == len(nums): return 0

            res = dfs(i+1, prev)

            if nums[i]>prev:
                res = max(res, 1+dfs(i+1, nums[i]))
            return res
        return dfs(0,float("-inf"))

# Time Complexity : O(2^n)
# Space Complexity : O(n)
        