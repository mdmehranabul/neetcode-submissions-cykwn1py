class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res=0
        target = k*threshold
        currsum=sum(arr[:k-1])
        l=0

        for r in range(k-1,len(arr)):
            currsum+=arr[r]
            if currsum>=target:
                res+=1
            currsum-=arr[l]
            l+=1
        return res

# Time Complexity - O(n)
# Space Complexity - O(1)