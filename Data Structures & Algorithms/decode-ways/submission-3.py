class Solution:
    def numDecodings(self, s: str) -> int:
        # def dfs(i):
        #     if i==len(s): return 1
        #     if s[i]=="0": return 0

        #     res=dfs(i+1)
        #     if i<len(s)-1:
        #         if (s[i]=="1" or (s[i]=="2" and s[i+1]<"7")):
        #             res+=dfs(i+2)            
        #     return res
        # return dfs(0)    

# Time Complexity - O(2^n)
# Space Complexity - O(n)

        def dfs(i, cache):
            if i in cache:
                return cache[i]
            
            if i == len(s): return 1
            if s[i] == "0": return 0

            cache[i]=dfs(i+1,cache)
            if i <len(s)-1:
                if s[i]=="1" or (s[i]=="2" and s[i+1]<"7"):
                    cache[i]+=dfs(i+2,cache)
            return cache[i]
        return dfs(0,{})

# Time Complexity - O(n)
# Space Complexity - O(n)