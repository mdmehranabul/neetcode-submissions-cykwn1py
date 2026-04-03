class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""

        countT,window={},{}
        res,resLen=[-1,-1],float('infinity') 
        l=0

        for i in t:
            countT[i]=1+ countT.get(i,0)

        have,need=0,len(countT)
        
        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            
            if c in countT and window[c]==countT[c]:
                have+=1
            
            while have==need:
                if(r+1-l)<resLen:
                    res=[l,r]
                    resLen=r+1-l
                
                window[s[l]]-=1

                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r=res

        return s[l:r+1] if resLen!=float('infinity') else ""