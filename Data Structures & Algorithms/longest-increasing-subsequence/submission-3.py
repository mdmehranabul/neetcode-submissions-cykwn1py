class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # def dfs(i, prev):
        #     if i == len(nums): return 0

        #     res = dfs(i+1, prev)

        #     if nums[i]>prev:
        #         res = max(res, 1+dfs(i+1, nums[i]))
        #     return res
        # return dfs(0,float("-inf"))

# Time Complexity : O(2^n)
# Space Complexity : O(n)

        def dfs(i, prev, cache):
            if (i,prev) in cache: return cache[(i,prev)]
            if i == len(nums): return 0

            cache[(i,prev)] = dfs(i+1, prev, cache)

            if nums[i]>prev:
                cache[(i,prev)] = max(cache[(i,prev)], 1+dfs(i+1, nums[i], cache))
            return cache[(i,prev)]
        return dfs(0,float("-inf"),{})

# Time Complexity : O(n^2)
# Space Complexity : O(n^2)