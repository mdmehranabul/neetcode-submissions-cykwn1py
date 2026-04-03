class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        def dfs(i, currset):
            if i==len(nums):
                res.append(currset.copy())
                return
            
            currset.append(nums[i])
            dfs(i+1, currset)

            while (i+1) < len(nums) and nums[i]==nums[i+1]:
                i+=1
            
            currset.pop()
            dfs(i+1, currset)
        
        dfs(0,[])
        return res
        