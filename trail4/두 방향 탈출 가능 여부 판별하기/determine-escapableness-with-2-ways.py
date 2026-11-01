
n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [1, 0]
dy = [0, 1]

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return True

    visited[x][y] = True

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == 1 and not visited[nx][ny]:
                if dfs(nx, ny):
                    return True

    return False

if grid[0][0] == 0:
    print(0)
else:
    print(1 if dfs(0, 0) else 0)
