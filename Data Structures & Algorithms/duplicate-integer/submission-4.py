class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map=set()

        for n in nums:
            if n not in hash_map: hash_map.add(n)
            else: return True
        return False
         