class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l,r = 1, length-2

        # Find Peak

        while l<=r:
            m = (l+r)//2

            left, mid, right = mountainArr.get(m-1),mountainArr.get(m),mountainArr.get(m+1)

            if left<mid<right:
                l = m+1
            
            elif left>mid>right:
                r = m-1
            
            else:
                break
        
        peak = m

        # Search left

        l, r = 0, peak-1

        while l <= r:
            m = (l+r)//2
            val = mountainArr.get(m)
            if target == val:
                return m
            elif target>val:
                l = m+1
            else:
                r = m-1
            
        # Search right

        l,r = peak, length -1

        while l <=r:
            m=(l+r)//2
            val = mountainArr.get(m)
            print(val,target)
            if val == target:
                return m
            elif target>val:
                r = m-1
            else:
                l=m+1
        
        return -1

# Time Complexity = O(log n)
# Space Complexity = O(1)