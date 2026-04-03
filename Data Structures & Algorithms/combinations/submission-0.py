class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, currset):
            if k == len(currset):
                res.append(currset.copy())
                return
            
            if i>=(n+1):
                return
            
            currset.append(i)
            dfs(i+1, currset)

            currset.pop()
            dfs(i+1, currset)
        
        dfs(1,[])
        return res
        