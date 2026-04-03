class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # words = set(dictionary)

        # def dfs(i):
        #     if i==len(s): return 0

        #     res = 1 + dfs(i+1)

        #     for j in range(i, len(s)):
        #         if s[i:j+1] in words:
        #             res = min(res, dfs(j+1))
        #     return res
        # return dfs(0)

# Time Complexity - O(n * 2^n + m*k)
# Space Complexity - O(n + m*k)

        words = set(dictionary)

        def dfs(i,cache):
            if i in cache: return cache[i]
            if i==len(s): return 0

            res = 1 + dfs(i+1,cache)

            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    res = min(res, dfs(j+1,cache))
            cache[i]=res
            return res
        return dfs(0,{})
