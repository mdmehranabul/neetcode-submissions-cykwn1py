class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])
        pass_cnt =0
        minHeap =[]

        for t in trips:
            curr_pass, start, end = t

            while minHeap and minHeap[0][0]<=start:
                pass_cnt -=minHeap[0][1]
                heapq.heappop(minHeap)

            pass_cnt +=curr_pass
            if pass_cnt>capacity:
                return False
            heapq.heappush(minHeap, [end,curr_pass])
            
        return True

# Time Complexity - O(nlogn)
# Space Complexity - O(n)



        