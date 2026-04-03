class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currset, total):
            if total == target:
                res.append(currset.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            

            currset.append(nums[i])
            dfs(i, currset, total + nums[i])

            currset.pop()
            dfs(i+1, currset, total)
        
        dfs(0, [], 0)
        return res

        