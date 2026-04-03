class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def cansplit(mid):
            split=1
            currsum=0

            for n in nums:
                currsum+=n
                if currsum>mid:
                    currsum=n
                    split+=1
            return split<=k

        l,r = max(nums), sum(nums)
        res = r

        while l<=r:
            mid = l + (r-l)//2

            if cansplit(mid):
                res = min(res, mid)
                r = mid-1
            else:
                l=mid+1
        return res
        