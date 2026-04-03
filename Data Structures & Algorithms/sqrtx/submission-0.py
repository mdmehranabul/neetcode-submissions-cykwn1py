class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=1,x
        res=0

        while l<=r:
            mid = l + (r-l)//2

            if mid**2==x:
                return mid
            elif mid**2>x:
                r=mid-1
            else:
                l=mid+1
                res=mid
        return res

# Time Complexity - O(log n)
# Space Complexity - O(1)
