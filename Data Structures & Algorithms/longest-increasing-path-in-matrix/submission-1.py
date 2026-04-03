class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # lip=0
        # ROWS, COLS = len(matrix), len(matrix[0])
        # def dfs(r,c,prev):
        #     if (r<0 or r>=ROWS or c<0 or c>=COLS or prev>=matrix[r][c]): return 0
        #     res= 1
        #     res = max(res,1 + dfs(r+1, c, matrix[r][c]))
        #     res = max(res,1 + dfs(r-1, c, matrix[r][c]))
        #     res = max(res,1 + dfs(r, c-1, matrix[r][c]))
        #     res = max(res,1 + dfs(r, c+1, matrix[r][c]))
        
        #     return res
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         lip = max(lip,dfs(r,c,float("-inf")))
        # return lip

# Time Complexity - O(m x n x 4^(m+n))
# Space Complexity - O(m x n)

        lip=0
        ROWS, COLS = len(matrix), len(matrix[0])
        cache={}
        def dfs(r,c,prev):
            if (r,c,prev) in cache: return cache[(r,c,prev)]
            if (r<0 or r>=ROWS or c<0 or c>=COLS or prev>=matrix[r][c]):
                return 0
            res= 1
            res = max(res,1 + dfs(r+1, c, matrix[r][c]))
            res = max(res,1 + dfs(r-1, c, matrix[r][c]))
            res = max(res,1 + dfs(r, c-1, matrix[r][c]))
            res = max(res,1 + dfs(r, c+1, matrix[r][c]))

            cache[(r,c,prev)] = res
            return cache[(r,c,prev)]
        
        for r in range(ROWS):
            for c in range(COLS):
                lip = max(lip,dfs(r,c,float("-inf")))
        return lip

# Time Complexity - O(m x n)
# Space Complexity - O(m x n)