class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l,r=0,1
        prev = ""
        res=1

        while r <len(arr):
            if arr[r-1]>arr[r] and prev!=">":
                prev = ">"
                res=max(res, r+1-l)
                r+=1
            elif arr[r-1]<arr[r] and prev!="<":
                prev = "<"
                res=max(res, r+1-l)
                r+=1
            else:
                r = r+1 if arr[r-1]==arr[r] else r
                prev=""
                l = r-1
        return res

# Time Complexity - O(n)
# Space Complexity - O(1)