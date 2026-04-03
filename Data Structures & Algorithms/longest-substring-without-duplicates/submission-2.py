class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        l=0
        charset=set()

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            res= max(r+1-l,res)
        return res


# Time Complexity - O(n)
# Space Complexity - O(m) - m -> is the total number of unique characters in the string.