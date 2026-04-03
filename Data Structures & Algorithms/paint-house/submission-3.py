class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # n = len(costs)

        # def dfs(i,prev):
        #     if i == n: return 0

        #     res= float("inf")
        #     for c in range(3):
        #         if c == prev:
        #             continue
                
        #         res = min(res, costs[i][c] + dfs(i+1,c))
        #     return res

        # return dfs(0,-1)

# Time Complexity - O(2^n)
# Space Complexity - O(n)

        n = len(costs)

        def dfs(i,prev,cache):
            if (i, prev) in cache: return cache[(i,prev)]
            if i == n: return 0

            res= float("inf")
            for c in range(3):
                if c == prev:
                    continue
                
                res = min(res, costs[i][c] + dfs(i+1,c, cache))
                cache[(i,prev)] = res

            return res

        return dfs(0,-1,{})

# Time Complexity - O(n)
# Space Complexity - O(n)