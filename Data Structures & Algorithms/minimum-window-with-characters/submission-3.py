class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        window_hash, count_hash={},{}
        res, reslen=[-1,-1],float("inf")

        for c in t:
            count_hash[c]=1+count_hash.get(c,0)

        have, need = 0, len(count_hash)

        l=0
        for r in range(len(s)):
            if s[r] in count_hash:
                window_hash[s[r]] = 1 + window_hash.get(s[r],0)
            if s[r] in count_hash and window_hash[s[r]] == count_hash[s[r]]:
                have+=1
            
            while have == need:

                if (r+1-l)<reslen:
                    reslen = r+1-l
                    res=[l,r]
                if s[l] in window_hash:
                    window_hash[s[l]]-=1
                if s[l] in count_hash and window_hash[s[l]] < count_hash[s[l]]:
                    have-=1
                l+=1
        
        l,r = res
        return s[l:r+1] if reslen!=float("infinity") else ""