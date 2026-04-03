class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # minHeap=[]
        
        # for n in nums:
        #     heapq.heappush(minHeap,-n)
        
        # while k:
        #     res = heapq.heappop(minHeap)
        #     k-=1
        # return -res

# Time Complexity - O(nlogn)
# Space Complexity - O(n)

        minHeap = []

        for n in nums:
            heapq.heappush(minHeap,n)
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        return minHeap[0]

# Time Complexity - O(nlogk)
# Space Complexity - O(k)