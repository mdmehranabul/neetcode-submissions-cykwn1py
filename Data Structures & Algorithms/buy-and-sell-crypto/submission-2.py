class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=l+1
        maxprof=0

        while r<len(prices):
            prof=prices[r]-prices[l]
            if prof<0:
                l=r    
            else:
                maxprof=max(maxprof,prof)
            r+=1
        return maxprof