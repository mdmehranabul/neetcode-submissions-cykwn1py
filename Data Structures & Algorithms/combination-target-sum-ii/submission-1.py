class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, currset, total):

            if target == total:
                res.append(currset.copy())
                return
            
            if i>= len(candidates) or total>target:
                return
            
            currset.append(candidates[i])
            dfs(i+1, currset, total + candidates[i])

            while i<len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1
            currset.pop()
            dfs(i+1, currset, total)
        
        dfs(0,[],0)
        return res

        