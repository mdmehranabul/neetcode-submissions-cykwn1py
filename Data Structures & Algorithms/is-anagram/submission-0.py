class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res= sorted(s)==sorted(t)
        return res