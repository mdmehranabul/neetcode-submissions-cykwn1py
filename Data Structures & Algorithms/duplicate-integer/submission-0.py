class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res= len(nums)!= len(set(nums))
        return res


