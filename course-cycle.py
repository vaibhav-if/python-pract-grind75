class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, preq in prerequisites:
            preMap[crs].append(preq)

        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True

sol = Solution()
numCourses = 5
prerequisites = [[0,1],[0,2],[1,3],[1,4],[3,4]]
print(sol.canFinish(numCourses, prerequisites))
