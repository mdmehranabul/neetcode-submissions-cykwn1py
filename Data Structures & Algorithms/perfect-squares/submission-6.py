class Solution:
    def numSquares(self, n: int) -> int:
        
        # def dfs(total):
        #     if total == 0: return 0
        #     res = float("inf")
        #     for i in range(1,total+1):
        #         if (i*i)>total:
        #             break
                
        #         res = min(res, 1+dfs(total - i*i))
        #     return res
        # return dfs(n)

# Time Complexity : O(n^sqrt(n))
# Space Complexity : O(n)

        def dfs(total,cache):
            if total in cache: return cache[total]
            if total == 0: return 0
            res = float("inf")
            for i in range(1,total+1):
                if (i*i)>total:
                    break
                
                res = min(res, 1+dfs(total - i*i, cache))
                cache[total]=res
            return res
        return dfs(n,{})

# Time Complexity : O(n x sqrt(n))
# Space Complexity : O(n)