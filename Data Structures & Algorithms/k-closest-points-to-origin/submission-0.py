class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap,res=[],[]

        for x, y in points:
            dis_sq=x**2 + y**2
            minheap.append([dis_sq,x,y])
        
        heapq.heapify(minheap)

        while k>0:
            dis_sq,x,y=heapq.heappop(minheap)
            res.append([x,y])
            k-=1
        return res

        