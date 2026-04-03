class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # def dfs(i,buying):
        #     if i>=len(prices):
        #         return 0
            
        #     if buying:
        #         buy = dfs(i+1, not buying) - prices[i]
        #         cooldown = dfs(i+1, buying)
        #         return max(buy, cooldown)
        #     else:
        #         sell = dfs(i+2, not buying) + prices[i]
        #         cooldown = dfs(i+1, buying)
        #         return max(sell, cooldown)
        # return dfs(0, True)

# Time Complexity : O(2^n)
# Space Complexity : O(n)

        def dfs(i,buying,cache):
            if i>=len(prices):
                return 0
            if (i,buying) in cache:
                return cache[(i,buying)]
            
            if buying:
                buy = dfs(i+1, not buying, cache) - prices[i]
                cooldown = dfs(i+1, buying, cache)
                cache[(i,buying)] = max(buy, cooldown)
                return cache[(i,buying)]
            else:
                sell = dfs(i+2, not buying, cache) + prices[i]
                cooldown = dfs(i+1, buying, cache)
                cache[(i,buying)] = max(sell, cooldown)
                return cache[(i,buying)]
        return dfs(0, True,{})

# Time Complexity : O(n)
# Space Complexity : O(n)