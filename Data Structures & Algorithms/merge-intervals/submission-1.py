class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        res=[intervals[0]]
        print(intervals)
        for start, end in intervals[1:]:
            last_end = res[-1][1]

            if last_end>=start:
                res[-1][1]=max(last_end,end)
            else:
                res.append([start, end])
        return res

# Time Complexity - O(nlogn)
# Space Complexity - O(1) or O(n)