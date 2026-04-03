class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_hash={i:[] for i in range(numCourses)}
        visited, cycle=set(),set()
        output=[]

        for crs,pre in prerequisites:
            course_hash[crs].append(pre)


        def dfs(crs):
            if crs in cycle: return False
            if crs in visited: return True

            cycle.add(crs)

            for pre in course_hash[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)

            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return []
        return output
        

