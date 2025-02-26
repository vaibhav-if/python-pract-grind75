class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        def markNeighbours(i, j, grid):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
                return

            grid[i][j] = "0"

            markNeighbours(i+1, j, grid)
            markNeighbours(i, j+1, grid)
            markNeighbours(i-1, j, grid)
            markNeighbours(i, j-1, grid)
        
        l = len(grid)
        l_row = len(grid[0])
        count = 0

        for i in range(l):
            for j in range(l_row):
                if grid[i][j] == "1":
                    count += 1
                    markNeighbours(i, j, grid)

        return count

sol = Solution()
print(sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))