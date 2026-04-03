class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # def dfs(amount):
        #     if amount ==0: return 0

        #     res = float("inf")

        #     for coin in coins:
        #         if (amount - coin) >=0:
        #             res = min(res, 1 + dfs(amount - coin))
        #     return res
        # res = dfs(amount)
        # return res if res != float("inf") else -1

# Time Complexity - O(n^t)
# Time Complexity - O(t)

        def dfs(amount, cache):
            if amount in cache:
                return cache[amount]
            if amount ==0: return 0

            res = float("inf")

            for coin in coins:
                if (amount-coin)>=0:
                    res = min(res, 1 + dfs(amount-coin,cache))
            
            cache[amount]=res
            return res
        
        res = dfs(amount,{})
        return -1 if res == float("inf") else res
