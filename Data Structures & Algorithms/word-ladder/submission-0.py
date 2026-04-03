class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        wordList.append(beginWord)
        visited=set([beginWord])
        q=deque([beginWord])
        res=1
        neigh=collections.defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                neigh[pattern].append(word)

        while q:
            for j in range(len(q)):
                word=q.popleft()
                if word==endWord: return res

                for k in range(len(word)):
                    pattern=word[:k]+"*"+word[k+1:]
                    for neighword in neigh[pattern]:
                        if neighword not in visited:
                            visited.add(neighword)
                            q.append(neighword)
            res+=1
        return 0




        