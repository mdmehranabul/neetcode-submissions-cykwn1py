class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        coursehash={i:[] for i in range(numCourses)}
        visited=set()

        for crs,pre in prerequisites:
            coursehash[crs].append(pre)

        def dfs(crs):
            if crs in visited: return False
            if coursehash[crs]==[]: return True
            visited.add(crs)

            for pre in coursehash[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            coursehash[crs]==[]
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

        