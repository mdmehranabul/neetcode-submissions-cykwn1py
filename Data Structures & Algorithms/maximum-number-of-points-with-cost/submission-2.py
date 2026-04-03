class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # m, n = len(points), len(points[0])

        # def dfs(r,c):
        #     if r == m-1: return 0

        #     res = 0 
        #     for col in range(n):
        #         res = max(res, points[r+1][col] - abs(col-c) + dfs(r+1, col))
        #     return res
        
        # ans = 0
        # for c in range(n):
        #     ans = max(ans, points[0][c] + dfs(0,c))
        # return ans

# Time Complexity - O(n^m)
# Space Complexity - O(m)

        ROWS, COLS = len(points), len(points[0])
        row = points[0]

        for r in range(1, ROWS):
            next_row = points[r].copy()
            left, right = [0]*COLS, [0]*COLS

            left[0] = row[0]
            for c in range(1, COLS):
                left[c]=max(row[c], left[c-1]-1)
            
            right[COLS-1] = row[COLS-1]
            for c in range(COLS-2, -1, -1):
                right[c] = max(row[c], right[c+1]-1)
        
            for c in range(COLS):
                next_row[c]+=max(left[c], right[c])
            row = next_row
        return max(row)
        