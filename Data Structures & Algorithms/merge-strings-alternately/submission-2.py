class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # i,j=0,0
        # res=""

        # while i<len(word1) and j<len(word2):
        #     res+=word1[i]+word2[j]
        #     i,j=i+1,j+1
        
        # if i<len(word1):
        #     res+=word1[i:]
        # if j<len(word2):
        #     res+=word2[j:]

        # return res

# Time Complexity - O(m+n)
# Space Complexity - O(m+n) for output string
        m, n = len(word1), len(word2)
        res=[]

        for i in range(max(m,n)):
            if i<m:
                res.append(word1[i])
            if i<n:
                res.append(word2[i])
        return "".join(res)