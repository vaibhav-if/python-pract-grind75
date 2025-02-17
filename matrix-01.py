from collections import deque

def updateMatrix(mat: list[list[int]]) -> list[list[int]]:
    m = len(mat)
    n = len(mat[0])
    queue = deque()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(0, m):
        for j in range(0, n):
            if mat[i][j] == 0:
                queue.append((i, j))
            else:
                mat[i][j] = -1 

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = dx + x, dy + y

            if (0 <= nx < m and 0 <= ny < n) and mat[nx][ny] == -1:
                mat[nx][ny] = mat[x][y] + 1
                queue.append([nx, ny])
            
            print(queue)
            print(mat)

    return mat
            
            

print(updateMatrix([[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]))