class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, perms =[],[]
        count = {}
        for n in nums:
            count[n]=1+ count.get(n,0)

        def dfs():
            if len(nums)==len(perms):
                res.append(perms.copy())
                return
            
            for n in count:
                if count[n]>0 :
                    perms.append(n)
                    count[n]-=1

                    dfs()

                    perms.pop()
                    count[n]+=1
        dfs()
        return res

        