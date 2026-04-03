class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        curr=[]

        def dfs(i,curr,total):
            if target==total:
                res.append(curr.copy())
                return
            if i>=len(nums) or total>target:
                return
            
            # Adding
            curr.append(nums[i])
            dfs(i,curr,total+nums[i])

            # Not adding
            curr.pop()
            dfs(i+1,curr,total)
        
        dfs(0,curr,0)
        return res
        