class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        res=0
        l=0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            res=max(res,r+1-l)
        return res