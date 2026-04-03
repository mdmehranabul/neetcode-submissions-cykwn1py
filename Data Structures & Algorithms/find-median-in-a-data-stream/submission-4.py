class MedianFinder:

    def __init__(self):
        self.small, self.large = [],[]  

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-1*num)

        if self.large and self.small and -1*self.small[0]>self.large[0]:
            val = -1* heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        if len(self.small)>len(self.large)+1:
            val = -1* heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        
        if len(self.large)>len(self.small)+1:
            val = -1*heapq.heappop(self.large)
            heapq.heappush(self.small,val)

    def findMedian(self) -> float:

        if len(self.small)>len(self.large):
            return -1*self.small[0]
        elif len(self.small)<len(self.large):
            return self.large[0]
        else:
            return (self.large[0] + -1* self.small[0])/2.0

# Time Complexity - O(mlog n) for addNum(), O(m) for findMedian()
# Space Complexity - O(n)
# m is the no. of function calls and n is the length of the array