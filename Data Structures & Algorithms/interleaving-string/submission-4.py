class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # if (len(s1) + len(s2))!=len(s3): return False

        # def dfs(i1,i2):
        #     if i1==len(s1) and  i2==len(s2) : return True

        #     if i1<len(s1) and s1[i1]==s3[i1+i2] and dfs(i1+1,i2): return True
        #     if i2<len(s2) and s2[i2]==s3[i1+i2] and dfs(i1,i2+1): return True
        #     return False
        
        # return dfs(0,0)

# Time Complexity : O(2^(m+n))
# Space Complexity : O(m+n)

        if (len(s1) + len(s2))!=len(s3): return False

        def dfs(i1,i2,cache):
            if (i1,i2) in cache:
                return cache[(i1,i2)]

            if i1==len(s1) and  i2==len(s2) :
                cache[(i1,i2)] = True
                return cache[(i1,i2)]

            if i1<len(s1) and s1[i1]==s3[i1+i2] and dfs(i1+1,i2,cache):
                cache[(i1,i2)] = True
                return cache[(i1,i2)]

            if i2<len(s2) and s2[i2]==s3[i1+i2] and dfs(i1,i2+1,cache):
                cache[(i1,i2)] = True
                return cache[(i1,i2)]

            cache[(i1,i2)] = False
            return cache[(i1,i2)]
        
        return dfs(0,0,{})


        