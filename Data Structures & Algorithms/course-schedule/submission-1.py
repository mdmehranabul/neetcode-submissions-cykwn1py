class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap={i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        cycle =set()

        def dfs(crs):
            if preMap[crs]==[]:
                return True
            if crs in cycle:
                return False
            
            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            preMap[crs]=[]
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        