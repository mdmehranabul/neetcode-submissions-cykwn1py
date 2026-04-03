class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l=0
        window=0
        satisfied=0
        max_window=float("-inf")


        for r in range(len(customers)):
            if grumpy[r]:
                window+=customers[r]
            else:
                satisfied+=customers[r]
            
            if (r+1-l)>minutes:
                if grumpy[l]:
                    window-=customers[l]
                l+=1
            max_window=max(max_window,window)
        return satisfied + max_window
        

# Time Complexity - O(n)
# Space Complexity - O(1)