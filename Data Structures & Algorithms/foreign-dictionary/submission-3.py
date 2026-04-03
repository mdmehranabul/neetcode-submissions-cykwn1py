class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjlist={c:set() for w in words for c in w}
        #print(adjlist)
        
        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            minlen=min(len(w1),len(w2))

            if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]: return ""

            for j in range(minlen):
                if w1[j]!=w2[j]:
                    adjlist[w1[j]].add(w2[j])
                    break
            #print(adjlist)

        visit={}
        res=[]

        def dfs(c):
            if c in visit: return visit[c]
            visit[c]=True
            for nei in adjlist[c]:
                if dfs(nei): return True
            visit[c]=False
            res.append(c)
        
        for c in adjlist:
            if dfs(c): return ""

        res.reverse()
        return "".join(res)
                