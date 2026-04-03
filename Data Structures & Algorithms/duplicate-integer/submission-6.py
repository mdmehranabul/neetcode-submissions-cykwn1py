class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # num_set = set()

        # for n in nums:
        #     if n in num_set:
        #         return True
        #     else:
        #         num_set.add(n)
        
        # return False

# Time Complexity : O(n)
# Space Complexity : O(n)

        return len(set(nums)) < len(nums)

# Time Complexity : O(n)
# Space Complexity : O(n)