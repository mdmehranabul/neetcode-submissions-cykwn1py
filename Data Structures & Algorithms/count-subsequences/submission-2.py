class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # def dfs(i1,i2):
        #     if i2==len(t): return 1
        #     if i1==len(s): return 0

        #     if s[i1]==t[i2]:
        #         return dfs(i1+1, i2+1) + dfs(i1+1,i2)
        #     else:
        #         return dfs(i1+1,i2)
        
        # return dfs(0,0)

# Time Complexity : O(2^m)
# Space Complexity : O(m)

        def dfs(i1,i2,cache):
            if (i1,i2) in cache: cache[(i1,i2)]
            if i2==len(t): return 1
            if i1==len(s): return 0

            if s[i1]==t[i2]:
                cache[(i1,i2)] = dfs(i1+1, i2+1,cache) + dfs(i1+1,i2,cache)
                return cache[(i1,i2)]
            else:
                cache[(i1,i2)]= dfs(i1+1,i2,cache)
                return cache[(i1,i2)]
        
        return dfs(0,0,{})