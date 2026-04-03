class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # m,n = len(word1), len(word2)

        # def dfs(i,j):
        #     if i==m: return n-j
        #     if j==n: return m-i

        #     if word1[i]==word2[j]: return dfs(i+1,j+1)

        #     return 1+min(dfs(i,j+1), dfs(i+1,j), dfs(i+1,j+1))
        # return dfs(0,0)

# Time Complexity = O(3^(m+n))
# Space Complexity = O(m+n)

        m,n = len(word1), len(word2)

        def dfs(i,j,cache):
            if (i,j) in cache:
                return cache[(i,j)]
            if i==m:
                cache[(i,j)] = n-j
                return cache[(i,j)]
            if j==n:
                cache[(i,j)]=m-i
                return cache[(i,j)]

            if word1[i]==word2[j]:
                cache[(i,j)]=dfs(i+1,j+1,cache)
                return cache[(i,j)]

            cache[(i,j)] = 1+min(dfs(i,j+1,cache), dfs(i+1,j,cache), dfs(i+1,j+1,cache))
            return cache[(i,j)]
        return dfs(0,0,{})

# Time Complexity = O(m x n)
# Space Complexity = O(m x n)