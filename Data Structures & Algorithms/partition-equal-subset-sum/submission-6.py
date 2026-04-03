class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # if sum(nums)%2: 
        #     return False

        # def dfs(i, target):
        #     if i==len(nums): return target==0
        #     if target<0:
        #         return False
            
        #     return dfs(i+1,target) or dfs(i+1, target-nums[i])

        # return dfs(0, sum(nums)//2)

# Time Complexity : O(2^n)
# Space Complexity : O(n)

        if sum(nums)%2: return False

        def dfs(i,target, cache):
            if (i,target) in cache: return cache[(i,target)]
            if i ==len(nums): return target == 0

            if target<0: return False

            cache[(i,target)] = dfs(i+1, target, cache) or dfs(i+1, target-nums[i], cache)
            return cache[(i,target)]
        return dfs(0, sum(nums)//2, {})

# Time Complexity : O(n*target)
# Space Complexity : O(n*target)