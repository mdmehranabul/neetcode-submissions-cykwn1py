class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}

        for i,n in enumerate(nums):
            if n not in num_hash:
                num_hash[target-n]=i
            else:
                return [num_hash[n],i]


# nums 

# 0 3
# 1 4
# 2 5
# 3 6

# num_hash
# 4 0

