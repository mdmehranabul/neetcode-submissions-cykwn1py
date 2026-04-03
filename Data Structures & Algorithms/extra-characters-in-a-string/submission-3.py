class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            curr = self.root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(dictionary)
        def dfs(i,cache):
            if i in cache: return cache[i]
            if i==len(s): return 0

            res = 1 + dfs(i+1,cache)
            curr = trie.root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.word:
                    res = min(res,dfs(j+1,cache))
            cache[i]=res
            return res
        return dfs(0,{})

        # words = set(dictionary)

        # def dfs(i):
        #     if i==len(s): return 0

        #     res = 1 + dfs(i+1)

        #     for j in range(i, len(s)):
        #         if s[i:j+1] in words:
        #             res = min(res, dfs(j+1))
        #     return res
        # return dfs(0)

# Time Complexity - O(n * 2^n + m*k)
# Space Complexity - O(n + m*k)

        # words = set(dictionary)

        # def dfs(i,cache):
        #     if i in cache: return cache[i]
        #     if i==len(s): return 0

        #     res = 1 + dfs(i+1,cache)

        #     for j in range(i, len(s)):
        #         if s[i:j+1] in words:
        #             res = min(res, dfs(j+1,cache))
        #     cache[i]=res
        #     return res
        # return dfs(0,{})

# Time Complexity - O(n^3 + m*k)
# Space Complexity - O(n + m*k)



