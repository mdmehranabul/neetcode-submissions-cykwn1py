class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        L,R = 0,ROWS-1

        while L<=R:
            mid = (L+R)//2

            if target > matrix[mid][-1]:
                L=mid+1
            elif target < matrix[mid][0]:
                R=mid-1
            else:
                left = 0
                right = COLS-1

                while left<=right:
                    middle = (left+right)//2

                    if matrix[mid][middle] == target:
                        return True
                    elif matrix[mid][middle] > target:
                        right = middle - 1
                    else:
                        left = middle + 1
                return False
        return False        

# Time Complexity - O(log mn)
# Space Complexity - O(1)