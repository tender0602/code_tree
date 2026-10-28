n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

lst = []
answer =[]

for i in range(n-1):
    for j in range(m-1) :
        lst.append(grid[i][j])
        lst.append(grid[i+1][j])
        lst.append(grid[i][j+1])
        lst.append(grid[i+1][j+1])
        lst.remove(min(lst))
        answer.append(sum(lst))
        lst=[]


# 가로 일자 블럭
for i in range(n):
    for j in range(m-2):
        answer.append(
            grid[i][j] +
            grid[i][j+1] +
            grid[i][j+2]
        )

# 세로 일자 블럭
for i in range(n-2):
    for j in range(m):
        answer.append(
            grid[i][j] +
            grid[i+1][j] +
            grid[i+2][j]
        )

print(max(answer))


