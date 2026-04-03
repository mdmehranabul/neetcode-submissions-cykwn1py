class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for s in strs:
            charset=[0]*26
            for c in s:
                charset[ord(c)-ord("a")]+=1
            res[tuple(charset)].append(s)
        return res.values()
        