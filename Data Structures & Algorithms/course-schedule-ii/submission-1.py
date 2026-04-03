class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap={crs:[] for crs in range(numCourses)}
        visited, cycle = set(), set()
        output=[]

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            output.append(crs)
            visited.add(crs)
            cycle.remove(crs)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return output
        