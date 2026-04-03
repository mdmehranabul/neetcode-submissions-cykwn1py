class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap=[]

        for s in stones:
            minHeap.append(-s)
        
        heapq.heapify(minHeap)

        while len(minHeap)>1:
            s1 = heapq.heappop(minHeap)
            s2 = heapq.heappop(minHeap)
            
            diff = s1-s2
            if diff!=0:
                heapq.heappush(minHeap,diff)
        
        return -1*minHeap[0] if minHeap else 0

# Time Complexity - O(nlogn)
# Space Complexity - O(n)
