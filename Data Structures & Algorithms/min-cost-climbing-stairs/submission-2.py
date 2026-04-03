class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # def dfs(i):
        #     if i >=len(cost):
        #         return 0
            
        #     return cost[i] + min(dfs(i+1), dfs(i+2))
        # return min(dfs(0), dfs(1))
    
    # Time Complexity - O(2^n)
    # Space Complexity - O(n)

        def dfs(i, cache):
            if i in cache:
                return cache[i]
            
            if i>= len(cost):
                return 0
            
            cache[i] = cost[i] + min(dfs(i+1,cache), dfs(i+2, cache))
            return cache[i]
        return min(dfs(0,{}), dfs(1,{}))

        