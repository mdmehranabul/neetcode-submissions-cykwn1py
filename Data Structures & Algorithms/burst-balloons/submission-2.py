class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # nums = [1]+nums+[1]
        
        # def dfs(l,r):
        #     if l>r: return 0
        #     res=0
        #     for i in range(l, r+1):
        #         coins = nums[l-1]*nums[i]*nums[r+1]
        #         coins += dfs(l,i-1) + dfs(i+1,r)
        #         res = max(res,coins)

        #     return res

        # return dfs(1, len(nums)-2)

# Time Complexity : O(n x 2^n)
# Space Complexity : O(n x 2^n)
        
        nums = [1]+nums+[1]
        
        def dfs(l,r,cache):
            if (l,r) in cache: return cache[(l,r)]
            if l>r:
                cache[(l,r)] = 0
                return cache[(l,r)]

            res=0
            for i in range(l, r+1):
                coins = nums[l-1]*nums[i]*nums[r+1]
                coins += dfs(l,i-1,cache) + dfs(i+1,r,cache)
                res = max(res,coins)
                cache[(l,r)] =res

            return cache[(l,r)]

        return dfs(1, len(nums)-2,{})