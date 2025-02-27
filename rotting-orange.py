class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid:
            return -1
        
        fresh_oranges = 0
        rotten_queue = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    rotten_queue.append((r,c,0))

        minutes = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while rotten_queue:
            r,c,time = rotten_queue.pop(0)
            minutes = max(minutes, time)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    rotten_queue.append((nr, nc, time + 1))

        if fresh_oranges == 0:
            return minutes
        else:
            return -1


sol = Solution()
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
