class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # stoneSum= sum(stones)
        # target = stoneSum//2
        # def dfs(i, total):
        #     if total >=target or i==len(stones):
        #         return abs(total - (stoneSum - total))
            
        #     return min(dfs(i+1,total), dfs(i+1, total+stones[i]))
        # return dfs(0,0)

# Time Complexity : O(2^n)
# Space Complexity : O(min(m,n))

        stoneSum= sum(stones)
        target = stoneSum//2
        def dfs(i, total,cache):
            if (i, total) in cache: return cache[(i,total)]
            if total >=target or i==len(stones):
                cache[(i,total)] = abs(total - (stoneSum - total))
                return cache[(i,total)]
            
            cache[(i,total)] = min(dfs(i+1,total,cache), dfs(i+1, total+stones[i],cache))
            return cache[(i,total)]
        return dfs(0,0,{})

# Time Complexity : O(m x n)
# Space Complexity : O(m x n)
# where n is the number of stones and m is the sum of the weights of the stones.
