class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # if n==1: return nums[0]
        # def dfs(i,arr):
        #     if i>=len(arr):
        #         return 0           
        #     return max(arr[i]+dfs(i+2, arr), dfs(i+1,arr)) 
        # return max(dfs(0, nums[1:]), dfs(0, nums[:-1]))

# Time Complexity : O(2^n)
# Space Complexity : O(n)

        # if len(nums)==1: return nums[0]

        # def dfs(i, arr, cache):
        #     if i in cache:
        #         return cache[i]
        #     if i >=len(arr):
        #         return 0
            
        #     cache[i] = max(arr[i] + dfs(i+2, arr, cache), dfs(i+1, arr, cache))
        #     return cache[i]
        # return max(dfs(0, nums[1:], {}), dfs(0, nums[:-1], {}))

# Time Complexity : O(n)
# Space Complexity : O(n)

        if len(nums) == 1: return nums[0]

        def helper(arr):
            
            if len(arr)==1: return arr[0]
            dp = [0]*len(arr)
            dp[0], dp[1] = arr[0], max(arr[0],arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(arr[i]+ dp[i-2], dp[i-1])
            
            return dp[-1]
        
        return max(helper(nums[:-1]), helper(nums[1:]))

