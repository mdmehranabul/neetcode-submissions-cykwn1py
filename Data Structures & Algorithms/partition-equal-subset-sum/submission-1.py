class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2: return False
        dp=set()
        dp.add(0)

        target=sum(nums)//2

        for i in range(len(nums)-1,-1,-1):
            new_dp=set()
            for val in dp:
                if val+nums[i]==target: return True
                new_dp.add(val+nums[i])
                new_dp.add(val)
            dp=new_dp
        
        return False
        