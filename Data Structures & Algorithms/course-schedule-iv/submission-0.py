class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        res=[]

        for pre,crs in prerequisites:
            adj[crs].append(pre)
        
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs]=set()

                for pre in adj[crs]:
                    prereqMap[crs] |=dfs(pre)
                prereqMap[crs].add(crs)
            
            return prereqMap[crs]



        prereqMap={}
        for i in range(numCourses):
            dfs(i)
        
        for u, v in queries:
            res.append(u in prereqMap[v])
        
        return res


        