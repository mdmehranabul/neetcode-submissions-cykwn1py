class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col=len(matrix),len(matrix[0])

        top,bot=0,row-1
        while top<=bot:
            focus_row=(top+bot)//2

            if (target>matrix[focus_row][-1]):
                top=focus_row+1
            elif (target<matrix[focus_row][0]):
                bot=focus_row-1
            else:
                break

        r=(top+bot)//2
        L,U=0,col-1

        while(L<=U):
            mid=(L+U)//2
            if target<matrix[r][mid]:
                U=mid-1
            elif target>matrix[r][mid]:
                L=mid+1
            else:
                return True
        return False
            
        