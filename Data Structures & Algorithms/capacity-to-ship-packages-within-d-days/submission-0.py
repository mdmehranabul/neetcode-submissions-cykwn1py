class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights), sum(weights)
        res = float("infinity")
        
        def shipcap(mid):
            currcap=mid
            ship=1

            for w in weights:
                if currcap-w<0:
                    ship+=1
                    currcap = mid
                currcap-=w
            
            return ship<=days

        while l<=r:
            mid = (l+r)//2

            if shipcap(mid):
                r = mid-1
                res= min(res, mid)
            else:
                l = mid+1
        
        return res

        