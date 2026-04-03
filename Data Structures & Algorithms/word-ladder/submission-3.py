class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)
        res=1
        wordList.append(beginWord)
        visit=set([beginWord])
        q=deque([beginWord])

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] +"*"+word[i+1:]
                nei[pattern].append(word)
        print(nei)
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res     
                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]
                    for neiword in nei[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            res+=1
        return 0

        