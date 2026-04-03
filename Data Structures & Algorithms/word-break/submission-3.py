class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # def dfs(i):
        #     if i == len(s):
        #         return True
            
        #     for w in wordDict:
        #         if (i+len(w))<=len(s) and s[i:i+len(w)]==w:
        #             if dfs(i+len(w)): return True
        #     return False
        # return dfs(0)

# Time Complexity : O(t*m^n)
# Time Complexity : O(n)

        def dfs(i,cache):
            if i in cache:
                return cache[i]
            if i == len(s):
                cache[i] = True
                return cache[i]
            
            for w in wordDict:
                if (i+len(w))<=len(s) and s[i:i+len(w)]==w:
                    if dfs(i+len(w),cache):
                        cache[i] = True
                        return cache[i]
            cache[i] = False
            return cache[i]
        return dfs(0,{})