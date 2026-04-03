class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        
        original_color=image[sr][sc]
        
        ROWS, COLS = len(image), len(image[0])

        def dfs(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLS:
                return
            if image[r][c]!=original_color:
                return
            
            image[r][c]=color

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        dfs(sr,sc)
        return image

        