class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]!=".":
                    if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r//3,c//3)]:
                        return False
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    square[(r//3,c//3)].add(board[r][c])
        return True
        

#Time Complexity - O(n^2)
#Space Complexity - O(n^2)