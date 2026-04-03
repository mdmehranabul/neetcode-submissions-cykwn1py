class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curr_min,curr_max=1,1

        for n in nums:
            curr_max,curr_min=max(n*curr_max,n*curr_min,n),min(n*curr_max,n*curr_min,n)
            res=max(curr_max,res)
        return res
        