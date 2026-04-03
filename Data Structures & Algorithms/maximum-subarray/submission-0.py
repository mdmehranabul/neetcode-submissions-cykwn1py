class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub=nums[0]
        curr_sum=0

        for n in nums:
            if curr_sum<0: curr_sum=0
            curr_sum+=n
            maxsub=max(maxsub,curr_sum)
        return maxsub
        