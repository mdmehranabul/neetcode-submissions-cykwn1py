class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set(nums)
        length=1
        longest=0

        for n in nums:
            length=1
            if n-1 not in hashset:
                
                while n+length in hashset:
                    length+=1
                longest=max(longest,length)
        return longest
        