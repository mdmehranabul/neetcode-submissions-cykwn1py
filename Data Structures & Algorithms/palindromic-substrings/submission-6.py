class Solution:
    def countSubstrings(self, s: str) -> int:
        # res=0

        # for i in range(len(s)):
        #     l,r = i,i

        #     while l>=0 and r<len(s) and s[l]==s[r]:
        #         res+=1
        #         l-=1
        #         r+=1
            
        #     l,r=i,i+1
        #     while l>=0 and r<len(s) and s[l]==s[r]:
        #         res+=1
        #         l-=1
        #         r+=1
        # return res

# Time Complexity : O(n^2)
# Space Complexity : O(1)

        def palin_len(l,r):
            res=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            return res

        res=0
        for i in range(len(s)):
            res+=palin_len(i,i) + palin_len(i,i+1)
        
        return res

# Time Complexity : O(n^2)
# Space Complexity : O(1)