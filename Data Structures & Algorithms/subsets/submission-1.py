class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        currset = []

        def dfs(i):
            if i>=len(nums):
                res.append(currset.copy())
                return
            
            currset.append(nums[i])
            dfs(i+1)

            currset.pop()
            dfs(i+1)
        dfs(0)
        return res
        