class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        recolor = 0
        res = k

        for r in range(len(blocks)):
            if blocks[r]=="W":
                recolor+=1
            if (r+1-l) == k:
                res= min(res,recolor)
                recolor-=1 if blocks[l]=="W" else 0
                l+=1

        return res

# Time Complexity - O(n)
# Space Complexity - O(1)