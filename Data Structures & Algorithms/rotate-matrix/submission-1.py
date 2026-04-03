class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,r=0,len(matrix)-1

        while l<r:
            top,bottom=l,r

            for i in range(r-l):
                topleft=matrix[top][l+i]
                matrix[top][l+i]=matrix[bottom-i][l]
                matrix[bottom-i][l]=matrix[bottom][r-i]
                matrix[bottom][r-i]=matrix[top+i][r]
                matrix[top+i][r]=topleft
            r-=1
            l+=1

# Time Complexity - O(n^2)
# Space Complexity - O(1)


        