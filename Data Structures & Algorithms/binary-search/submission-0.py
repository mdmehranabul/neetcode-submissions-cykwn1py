class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,U=0,len(nums)-1
        
        while L<=U:
            M=L + ((U - L) // 2)
            if(target==nums[M]):
                return M
            elif (target>nums[M]):
                L=M+1
            else:
                U=M-1
        return -1
            
        